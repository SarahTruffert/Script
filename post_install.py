import os
#!/bin/bash

print("UBUNTU POST-INSTALL SCRIPT")
print("Updating APT...")
os.system("sudo apt-get update") 
os.system("clear")
print("Installing base packages")
os.system("sudo apt-get install --yes git git-extras build-essential python3-pip htop glances")
os.system("-O vscode.deb")
os.system("sudo dpkg -i ./vscode.deb")
os.system("sudo apt-get install -f")
os.system("sudo snap install discord")