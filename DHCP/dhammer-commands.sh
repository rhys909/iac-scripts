#! /bin/bash

git clone https://go.googlesource.com/go goroot
cd goroot
cd src
./all.bash

sudo ./dhammer dhcpv4 --interface eth0 --mac-count 10000 --rps 1000 --maxlife 0


