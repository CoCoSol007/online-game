import socket


connexion = socket.socket()
host = '192.168.1.40'
port = 2004
connexion.connect((host, port))

import os
# récupérer le chemin du répertoire courant.
path = os.getcwd()

from programe_game.game import main

main(connexion, path)