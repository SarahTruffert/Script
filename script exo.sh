#!/bin/bash
echo "UBUNTU POST-INSTALL SCRIPT"
echo "Updating APT..."
sudo apt-get update 
clear
echo "Installing base packages"
sudo apt-get install --yes git git-extras build-essential python3-pip htop glances
-O vscode.deb
sudo dpkg -i ./vscode.deb
sudo apt-get install -f
