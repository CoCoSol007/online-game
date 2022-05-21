from multiprocessing import connection
import pygame
from telechargement_image import download
import socket
from player import envoi

class Enemi(pygame.sprite.Sprite):
    # Constructeur de la classe
    def __init__(self, cliensocket ):
        super().__init__()
        self.images = download("red")
        
        
        self.image = self.images[15]
        self.rect = self.image.get_rect()

        self.rect.center = (700, 300)
        self.direction = "<"

        
        self.ClientMultiSocket = cliensocket

        self.positionX = - 300000
        self.positionY = 100
        self.ancienne_positionX = self.positionX
        self.ancienne_positionY = self.positionY
        
        self.here = True
        self.move = False

        self.group = pygame.sprite.Group(self)

    def update(self, tic):

        if self.here:
            
            if tic % 1 == 0:

                if not self.move:
                    if self.direction == ">":
                        self.image = self.images[0]
                    else:
                        self.image = self.images[9]

                else:
                    if self.direction == ">":
                        self.image = self.images[int(tic)]
                    else:
                        tic += 9
                        self.image = self.images[int(tic)]

            

            self.rect.center = self.positionX,self.positionY

    

    def recevoir_donnees(self):
        
        self.ancienne_positionX = self.positionX
        self.ancienne_positionY = self.positionY
        
        donnees_recus = self.ClientMultiSocket.recv(128).decode('utf-8')

        

        
        
 
        donnees_recus = donnees_recus.split(',')
        self.positionX = int(donnees_recus[0])
        self.positionY = int(donnees_recus[1])
                

        if self.ancienne_positionX < self.positionX:
            self.direction = "<"
            self.move = True 
        elif self.ancienne_positionX > self.positionX:
            self.direction = ">"
            self.move = True 
        elif self.ancienne_positionY != self.positionY:
            self.move = True 
        else:
            self.move = False

        
        
            
        
            
            
            
            