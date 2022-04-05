#! /bin/bash

echo "Update the system"
apt-get update -y
apt-get upgrade -y

echo "Begin Pi-Hole installation now"
#The below command calls upon Pi-Holes own automated bash basic install file 
curl -sSL https://install.pi-hole.net | bash

