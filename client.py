import socket


connexion = socket.socket()
host = '138.68.96.66'
port = 2004
connexion.connect((host, port))

import os
# récupérer le chemin du répertoire courant.
path = os.getcwd()

from programe_game.game import main

main(connexion, path)