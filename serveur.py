import socket
from _thread import *
import threading



ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0



def creer_un_thread( cible):

		thread = threading.Thread(target=cible)
		thread.daemon = True
		thread.start

ServerSideSocket.bind((host, port))

print('Socket is listening..')
ServerSideSocket.listen(5)


def transfert (client_envoi, client_reçoi):

    msg = reçoi(client_envoi)
    envoi(client_reçoi, msg)



def envoi(connection, msg):
    
    a = msg.encode("utf-8")
    connection.send(a)

def reçoi(connection):

    DataSorti = connection.recv(128).decode('utf-8') 
    if DataSorti == "stop":
        print("a")
    return DataSorti
    


Client1, adresse1 =  ServerSideSocket.accept()
print ("1 joueur ...")
Client2, adresse2 =  ServerSideSocket.accept() 
print ("2 jpueurs ...")



while True :
    creer_un_thread(transfert(Client1, Client2))
    creer_un_thread(transfert(Client2, Client1))
    