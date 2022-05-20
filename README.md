# local_xchange

#### script permettant le partage d'un dossier sur un réseau local en Python3.8

un vieux petit script que j'ai ressortie d'une clé USB perdue et enfin retrouvée (!!!), permettant de mettre en partage un dossier tout en laissant le choix du port de sortie à l'utilisateur.  
par défaut, le port de sortie sera le 8008, et il sera impossible de choisir un port en-dessous du numéro 1025, ni au dessus du numéro 65535 (question de sécurité).  
il utilise les modules threading, tkinter, socket et http.server et donne un bon exemple concret de l'utilisation d'un thread avec une fenetre tkinter.  

le script contient deux classes : un thread, permettant d'activer ou de désactiver le serveur Python, et une classe principale contenant la fenetre principale ainsi que les fonctionnalités de celle-ci.  

par sécurité, si l'utilisateur quitte le programme sans refermer le socket de connexion, il sera automatiquement fermé.  

le but est de pouvoir échanger rapidement des fichiers entre plusieurs pc en réseau local. il suffira pour cela de poser ce script dans le dossier à partager et de le démarrer.  

Daniel, le 20/05/2022.  

