#!/bin/bash

# Continuous monitoring loop
while true; do
    # Run the command and print the received packets on the physical layer with a comma at the end
    ethtool -S enp7s0np0 | grep -E 'tx_packets_phy' | awk '{print $2 ","}'

    # Sleep for 1 second before running the command again
    sleep 0.1
done
