#! /bin/bash

sudo ./dhammer dhcpv4 --interface eth0 --mac-count 10000 --rps 1000 --maxlife 0 --relay-target-server-ip 192.168.1.125 --relay-source-ip 192.168.1.1