#!/bin/bash
currentDir=$PWD

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
    mkdir /usr/share/stegbrute
    cp $PWD /usr/share/stegbrute
    echo "alias stegbrute='python3 /usr/share/steghidebrute/stegbrute-v1.0'" >> $HOME/.bash_aliases
    echo "Type \"stegbrute\" on the cmd!"
    stegbrute
fi
