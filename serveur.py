import socket
from _thread import *
import threading



ServerSideSocket = socket.socket()
host = ''
port = 2004




def creer_un_thread( cible):

		thread = threading.Thread(target=cible)
		thread.daemon = True
		thread.start

ServerSideSocket.bind((host, port))

print('serveur lancer...')
print("En ecoute ...")
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
        print ("Un joueur ces deconecté ...")
        print (str(len(all_client))+" joueur ...")
        print ("en attente de nouveau joueur ...")
        print ("mode hors ligne activer ...")
        all_client.remove(connection)

    

    return DataSorti
    
def console():
    input("==> ")
    


all_client = []

Client, adresse =  ServerSideSocket.accept()
all_client.append(Client)
print (str(len(all_client))+" joueur ...")

Client, adresse =  ServerSideSocket.accept() 
all_client.append(Client)
print (str(len(all_client))+" joueur ...")



while True :
    try:
        creer_un_thread(transfert(all_client[0], all_client[1]))
        creer_un_thread(transfert(all_client[1], all_client[0]))
        #creer_un_thread (console())
    except:
        Client, adresse =  ServerSideSocket.accept()
        all_client.append(Client)
        print (str(len(all_client))+" joueur ...")
