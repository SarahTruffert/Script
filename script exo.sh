#./nom_du_script.sh, faite la commande : sed -i -e 's/\r$//'  nom_du_script.sh
#Pour lancer script 
#!/bin/bash

echo "UBUNTU POST-INSTALL SCRIPT"
echo "Updating APT..."
sudo apt-get update 
clear
#Pour intaller Git 
echo "Installing base packages"
sudo apt-get install --yes git git-extras build-essential python3-pip htop glances
#Pour installer visual code 
-O vscode.deb
sudo dpkg -i ./vscode.deb
sudo apt-get install -f
#Pour installer code discord 
