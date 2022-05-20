#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys
import socket
import http.server
from tkinter import *
from tkinter.messagebox import *
from threading import *

###############################################################################
### classe thread permettant l'éxécution du serveur en boucle
###############################################################################
class Local_Servitude(Thread):
    ### initialisation du thread
    def __init__(self, port_num):
        Thread.__init__(self)
        self.port_num = port_num
        self.serveur_line = None
    ### activation du thread
    def run(self):
        server_address = ("", self.port_num)
        server = http.server.HTTPServer
        handler = http.server.CGIHTTPRequestHandler
        handler.cgi_directories = [""]
        self.serveur_line = server(server_address, handler)
        self.serveur_line.serve_forever()
    ### arret du thread
    def stop(self):
        if self.serveur_line != None:
            self.serveur_line.shutdown()

###############################################################################
### classe principale
###############################################################################
class Local_LAN(Tk):
    ###########################################################################
    ### fenetre principale de l'application
    ###########################################################################
    def __init__(self):
        ### variables de l'application
        self.status = False
        self.local_ip = socket.gethostbyname_ex(socket.gethostname())[2]
        self.donne_acces = None
        ### fenetre de l'application
        Tk.__init__(self)
        self.title("Echange Local Intranet")
        self.minsize(width = 300, height = 150)
        self.resizable(width = False, height = False)
        ### éléments de la fenetre
        ### concernant le port de sortie
        libelle_01 = Label(self, text = "Port de sortie : ")
        libelle_01.grid(row = 1, column = 1)
        self.definition_port = Entry(self)
        self.definition_port.grid(row = 1, column = 2)
        self.definition_port.insert("end", "8008")
        ### concernant l'adresse IP du serveur
        libelle_02 = Label(self, text = "IP serveur : ")
        libelle_02.grid(row = 2, column = 1)
        self.id_serveur = Label(self, background = 'lightyellow',
                                text = str(self.local_ip[0]))
        self.id_serveur.grid(row = 2, column = 2)
        ### concernant le statut du serveur
        libelle_03 = Label(self, text = "Status du serveur : ")
        libelle_03.grid(row = 3, column = 1)
        self.stat_serveur = Label(self, background = 'lightyellow',
                                  text = "Inactif")
        self.stat_serveur.grid(row = 3, column = 2)
        ### boutons de la fenetre
        activation_serveur = Button(self, text = "Activer / Désactiver",
                                    command = self.serv_line)
        activation_serveur.grid(row = 4, column = 1, columnspan = 2)
        info_appli = Button(self, text = "Info de l'appli", command = self.info)
        info_appli.grid(row = 5, column = 1, columnspan = 2)
        quitter_appli = Button(self, text = "Quitter", command = self.quitter)
        quitter_appli.grid(row = 6, column = 1, columnspan = 2)
        ### bouclage et fin de l'application
        self.mainloop()
        try:
            self.destroy()
        except TclError:
            sys.exit()

    ###########################################################################
    ### fonctions de l'application
    ###########################################################################
    def serv_line(self):
        # récupération de la valeur 
        PORT = self.definition_port.get()                      
        if self.status == False:
            # essai et conditions de connexion
            try:
                # voir si le port spécifié est valide
                PORT = int(PORT)
                # si tel est le cas, vérifié le numéro de sortie
                if PORT >= 1025 and PORT <= 65535 :
                    # changer les variables de la classe
                    self.stat_serveur.configure(text = "Actif") 
                    self.status = True
                    # si ok, création du thread-serveur
                    self.donne_acces = Local_Servitude(PORT)
                    # lancement du thread-serveur 
                    self.donne_acces.start()
                    # informe l'utilisateur que le partage est actif
                    showinfo("okay", "Le partage est en cours.")
                # si numéro de sortie pas valide
                else:                                           
                    showwarning("heum...",
                                "Spécifiez un port entre 1025 et 65535")
            # si la valeur n'est pas un nombre
            except:                                            
                showwarning  ("heum..",
                              "Spécifiez un numéro de port valide !")
        # si la connexion est déjà établie, referme la
        else:                                                   
            self.status = False
            self.stat_serveur.configure(text = "Inactif")
            self.donne_acces.stop()
            self.donne_acces = None
            showinfo("Arret", "Le partage a été arreté.")

    def info(self):
        showinfo("Info sur l'appli...",
                 "Echange Local Intranet, créé par Meyer Daniel pour Linux sous Python 3, Mars 2020")

    def quitter(self):
        choix = askyesno("Fin ?", "Voulez vous quitter l'application ?")
        if choix == True:
            if self.status == True:
                self.donne_acces.stop()
                self.destroy()
            elif self.status == False:
                self.destroy()

###############################################################################
### execution du programme
###############################################################################
Local_LAN()

