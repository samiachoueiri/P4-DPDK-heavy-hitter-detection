#!/bin/bash

# Continuous monitoring loop
while true; do
    # Run the command and print the received and transmitted packets on the physical layer with a comma between them
    tx=$(ethtool -S enp7s0np0 | grep -E 'tx_packets_phy' | awk '{print $2}')
    rx=$(ethtool -S enp7s0np0 | grep -E 'rx_packets_phy' | awk '{print $2}')
    echo "$rx , $tx"
    # Sleep for 1 second before running the command again
    sleep 0.1
done