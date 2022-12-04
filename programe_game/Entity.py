import pygame
from programe_game.telechargement_image import download
from programe_game.bullet import bullet

class Entity(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        

        

class Player(pygame.sprite.Sprite):
    # Constructeur de la classe
    def __init__(self, conexion ):
        super().__init__()
        self.images = download("blue")
        a = []
        for i in range(0, len(self.images )):
            image = pygame.transform.scale(self.images[i], (128,128))
            a.append(image)
        self.images = a

        self.conexion = conexion
        
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.rect.center = (100, 300)

        self.mouvement = (0, 0)

        self.vitesse = 10
        self.direction = ">"

        self.score = 0
        self.type = "player"
        self.shoot = 0
    

    def update(self, tic):

        
        if tic % 1 == 0:

            if self.mouvement == (0,0):
                if self.direction == ">":
                    self.image = self.images[0]
                else:
                    self.image = self.images[3]

            else:
                if self.direction == ">":
                    self.image = self.images[int(tic)]
                else:
                    tic += 3
                    self.image = self.images[int(tic)]

        self.envoi_coo()

        

        self.rect.move_ip( self.mouvement)


    def envoi_coo(self):

        msg = str(self.rect.centerx) + "," + str(self.rect.centery) + "," + str(self.shoot)
        msg = msg.encode("utf-8")
        self.conexion.send(msg)
        self.shoot = 0

        
################################################################    


class Enemi(pygame.sprite.Sprite):
    # Constructeur de la classe
    def __init__(self, cliensocket ):
        super().__init__()

        self.images = download("red")
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
        self.direction = ">"
        self.type = "enemi"

        self.positionX = 100
        self.positionY = 300

        self.score = 0

        self.group = pygame.sprite.Group()
        self.type = "enemi"
        
        self.ClientMultiSocket = cliensocket
        
        self.here = True
        self.move = False


    def update(self, tic):

        if self.here:
            
            if tic % 1 == 0:

                if not self.move:
                    if self.direction == ">":
                        self.image = self.images[0]
                    else:
                        self.image = self.images[3]

                else:
                    if self.direction == ">":
                        self.image = self.images[int(tic)]
                    else:
                        tic += 3
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

        if donnees_recus[2] == "1":
            self.shoot()

    def shoot(self):
        self.group.add(bullet(self))

