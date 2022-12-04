import pygame
from telechargement_image import download

class Player(pygame.sprite.Sprite):
    # Constructeur de la classe
    def __init__(self, conection):
        super().__init__()
        self.images = download("blue")
        a = []
        for i in range(0, len(self.images )):
            image = pygame.transform.scale(self.images[i], (128,128))
            a.append(image)
        self.images = a
        
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.rect.center = (100, 300)

        self.mouvement = (0, 0)

        self.vitesse = 10

        self.score = 0
        self.direction = ">"
        self.conection = conection
        

    def update(self, tic):

        
        if tic % 1 == 0:

            if self.mouvement == (0,0):
                if self.direction == ">":
                    self.image = self.images[0]
                else:
                    self.image = self.images[9]

            else:
                if self.direction == ">":
                    self.image = self.images[int(tic)]
                else:
                    tic += 5
                    self.image = self.images[int(tic)]

        self.envoi_coo()

        

        self.rect.move_ip( self.mouvement)

    def envoi_coo(self):
        msg = str(self.rect.centerx) + "," + str(self.rect.centery)
        envoi(msg,self.conection)
    
def envoi(msg,conection):
        msg = msg
        msg = msg.encode("utf-8")
        conection.send(msg)
    
    

        
        

