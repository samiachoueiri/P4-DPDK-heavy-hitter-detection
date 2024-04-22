/*
Copyright 2023 Intel Corporation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

#include <core.p4>
#include <dpdk/pna.p4>


typedef bit<48>  EthernetAddress;

header ethernet_t {
    EthernetAddress dstAddr;
    EthernetAddress srcAddr;
    bit<16>         etherType;
}

header ipv4_t {
    bit<4>  version;
    bit<4>  ihl;
    bit<8>  diffserv;
    bit<16> totalLen;
    bit<16> identification;
    bit<3>  flags;
    bit<13> fragOffset;
    bit<8>  ttl;
    bit<8>  protocol;
    bit<16> hdrChecksum;
    bit<32> srcAddr;
    bit<32> dstAddr;
}

header tcp_t {
    bit<16> srcPort;
    bit<16> dstPort;
    bit<32> seqNo;
    bit<32> ackNo;
    bit<4>  dataOffset;
    bit<3>  res;
    bit<3>  ecn;
    bit<6>  ctrl;
    bit<16> window;
    bit<16> checksum;
    bit<16> urgentPtr;
}

struct empty_metadata_t {
}


//////////////////////////////////////////////////////////////////////
// Struct types for holding user-defined collections of headers and
// metadata in the P4 developer's program.
//
// Note: The names of these struct types are completely up to the P4
// developer, as are their member fields, with the only restriction
// being that the structs intended to contain headers should only
// contain members whose types are header, header stack, or
// header_union.
//////////////////////////////////////////////////////////////////////

struct main_metadata_t {
    // empty for this skeleton
    bit<16> data;
    bit<16> data1;
    bit<20> temp_count_0;
    bit<20> temp_count_1;
    bit<20> minimum;    
    bit<20> tmp;    
}

// User-defined struct containing all of those headers parsed in the
// main parser.
struct headers_t {
    ethernet_t ethernet;
    ipv4_t ipv4;
    tcp_t tcp;
}

control PreControlImpl(
    in    headers_t  hdr,
    inout main_metadata_t meta,
    in    pna_pre_input_metadata_t  istd,
    inout pna_pre_output_metadata_t ostd)
{
    apply {
        }
}

parser MainParserImpl(
    packet_in pkt,
    out   headers_t       hdr,
    inout main_metadata_t main_meta,
    in    pna_main_parser_input_metadata_t istd)
{
    state start {
        pkt.extract(hdr.ethernet);
        transition select(hdr.ethernet.etherType) {
            0x0800: parse_ipv4;
            default: accept;
        }
    }
    state parse_ipv4 {
        pkt.extract(hdr.ipv4);
        transition select(hdr.ipv4.protocol) {
            6: parse_tcp;
            default: accept;
        }
    
    } 
    state parse_tcp {
        pkt.extract(hdr.tcp);
        transition accept;
    }
}

control MainControlImpl(
    inout headers_t       hdr,           // from main parser
    inout main_metadata_t user_meta,     // from main parser, to "next block"
    in    pna_main_input_metadata_t  istd,
    inout pna_main_output_metadata_t ostd)
{   

    Hash<bit<16>> (PNA_HashAlgorithm_t.CRC16) h0;
    
    action a1() {
       user_meta.data = h0.get_hash((bit<16>)100, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
       //user_meta.data=0;
       //user_meta.data = (hdr.tcp.srcPort ^ hdr.tcp.dstPort ^ (bit<16>)hdr.ipv4.srcAddr[15:0] ^ hdr.ipv4.dstAddr[15:0]) % 32768;
    } 
    
    action a2() {
        user_meta.data1 = h0.get_hash((bit<16>)0, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);   
        //user_meta.data1=1;
        //user_meta.data1 = (hdr.tcp.srcPort + hdr.tcp.dstPort + (bit<16>)hdr.ipv4.srcAddr[15:0] + hdr.ipv4.dstAddr[15:0]) % 32768;

    }
    
    
    action drop () {
        drop_packet();
    }
    action L2_send_to_port (PortId_t port_id) {
        send_to_port(port_id);
    }
    // table L2_fwd {
    //     key = { hdr.ethernet.dstAddr: exact; }
    //     actions = { L2_send_to_port; drop; }
    //     default_action = drop;
    // }
    
    
    Register<bit<20>, bit<16>>(32768) reg0;
    Register<bit<20>, bit<16>>(32768) reg1;

    apply {
    
        if(hdr.tcp.isValid()) {
        
            // L2_fwd.apply();
            
            user_meta.minimum = 1048575;
            a1();
            a2();


            user_meta.temp_count_0 = reg0.read(user_meta.data);
            user_meta.temp_count_1 = reg1.read(user_meta.data1);

            user_meta.tmp = user_meta.minimum - user_meta.temp_count_0;
            if(user_meta.tmp > 0){
                user_meta.minimum = user_meta.temp_count_0;
            }

            user_meta.tmp = user_meta.minimum - user_meta.temp_count_1;
            if(user_meta.tmp > 0){
                user_meta.minimum = user_meta.temp_count_1;
            }




            
            if(user_meta.minimum > 100000){
                drop_packet();
            } 
            else {
                reg0.write(user_meta.data,user_meta.temp_count_0+1);
                reg1.write(user_meta.data1,user_meta.temp_count_1+1);
                
                bit<32> tmp_ip = hdr.ipv4.srcAddr;
                hdr.ipv4.srcAddr = hdr.ipv4.dstAddr;
                hdr.ipv4.dstAddr = tmp_ip;

                bit<48> tmp_mac = hdr.ethernet.srcAddr;
                hdr.ethernet.srcAddr = hdr.ethernet.dstAddr;
                hdr.ethernet.dstAddr = tmp_mac;

                if (istd.input_port == (PortId_t) 0){
                    send_to_port((PortId_t) 0);
                }
                else if (istd.input_port == (PortId_t) 1){
                    send_to_port((PortId_t) 1);
                }

            }
        } 
        else {
            send_to_port((PortId_t) 0);
        }
        
    }
}

control MainDeparserImpl(
    packet_out pkt,
    in    headers_t hdr,                // from main control
    in    main_metadata_t user_meta,    // from main control
    in    pna_main_output_metadata_t ostd)
{
    apply {
        pkt.emit(hdr.ethernet);
        pkt.emit(hdr.ipv4);
        pkt.emit(hdr.tcp);
    }
}

PNA_NIC(
    MainParserImpl(),
    PreControlImpl(),
    MainControlImpl(),
    MainDeparserImpl()
    ) main;