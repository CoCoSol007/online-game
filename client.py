from programe_game.game import main
import os
import socket


connexion = socket.socket()
host = 'localhost'
port = 2004
connexion.connect((host, port))

# récupérer le chemin du répertoire courant.
path = os.getcwd()


main(connexion, path)
