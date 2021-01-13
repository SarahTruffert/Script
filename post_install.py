import os
#!/bin/bash
#echo comme print sur python
print("UBUNTU POST-INSTALL SCRIPT")
print("Updating APT...")
#commentaire os systeme 
os.system("sudo apt-get update") 
os.system("clear")
print("Installing base packages")
os.system("sudo apt-get install --yes git git-extras build-essential python3-pip htop glances")
os.system("wget https://go.microsoft.com/fwlink/?LinkID=760868")
os.system("-O vscode.deb")
os.system("sudo dpkg -i ./vscode.deb")
os.system("sudo apt-get install -f")
os.system("sudo snap install discord")
