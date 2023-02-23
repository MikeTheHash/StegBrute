#!/bin/bash

if [ $USER != "root" ];
then
    echo "You need to run this as root"
elif [ $USER == "root" ];
then 
    sudo apt install steghide
    sudo apt install python3
    sudo apt install python3-pip
    sudo apt install pip
    pip install subprocess
    pip install argparse
    pip install colorama
fi