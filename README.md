# Script : installer environnement de travail :

#sudo= Executer qqch sur l'ordinateur comme super admin avec droits de modification.
#apt-get install : recherche uptdate et installe.

Pour lancer script :
#./nom_du_script.sh, faite la commande : sed -i -e 's/\r$//'  nom_du_script.sh


Début du script : 
#!/bin/bash

S'affiche sur ma console : 
echo "UBUNTU POST-INSTALL SCRIPT"
echo "Updating APT..."
sudo apt-get update 
clear

#Pour intaller Git et python et python Pip (librairies):
echo "Installing base packages"
sudo apt-get install --yes git git-extras build-essential python3-pip htop glances

#Pour installer visual code 
-O vscode.deb
sudo dpkg -i ./vscode.deb
sudo apt-get install -f

#Pour installer code discord 
sudo snap install discord
