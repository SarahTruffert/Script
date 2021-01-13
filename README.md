# Script : installer environnement de travail :

#sudo: Executer qqch sur l'ordinateur comme super admin avec droits de modification.
#apt-get install : recherche uptdate et installe.
#snap : Permet de chercher ce qui est téléchargeable et installable.
#get : à utiliser en ligne de commande = installation et la désinstallation de paquets en provenance d'un dépôt APT. 
#echo : comme print sur python 


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
build essential : Tout ce qui permet a Python de fonctionner 
echo "Installing base packages"
sudo apt-get install --yes git git-extras build-essential python3-pip htop glances

#Pour installer visual code 
-O vscode.deb
sudo dpkg -i ./vscode.deb
sudo apt-get install -f

#Pour installer code discord 
sudo snap install discord
