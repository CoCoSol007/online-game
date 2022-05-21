# On importe le module pygame
import pygame


from telechargement_image import download

class Player(pygame.sprite.Sprite):
    # Constructeur de la classe
    def __init__(self):
        super().__init__()
        self.images = download("blue")
        
        self.image = self.images[15]
        self.rect = self.image.get_rect()

        self.rect.center = (100, 300)

        self.mouvement = (0, 0)

        self.vitesse = 10

        self.score = 0
        self.direction = ">"
        
        

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
                    tic += 9
                    self.image = self.images[int(tic)]


        self.rect.move_ip( self.mouvement)
 


# On initialise pygame
pygame.init()

# On créé une horloge (pour les FPS)
horloge = pygame.time.Clock()




# On créé un écran pour notre programme (= une fenêtre)
ecran = pygame.display.set_mode( (800, 600) )



gravity = 1


# On définit le taux de rafraîchissement de la fenêtre
fps = 30

# On instancie un héros
player1 = Player()

# On créé un groupe où placer le héros
player1_groupe = pygame.sprite.Group()

# On ajoute le héros au groupe
player1_groupe.add(player1)

tic = 0

# On créé une variable pour sortir de la boucle principale
marche = True

# On met en place la boucle principale d'affichage
while marche:
    
    tic += 0.5

    if tic == 9:
        tic = 0
    
    # On récupère la liste des évènements actuels
    evenements = pygame.event.get()

    # On fait le tour de la liste des évènements
    for evenement in evenements:
        # Si l'évènement actuel est de type QUIT
        if evenement.type == pygame.QUIT:
            # On sort de la boucle
            marche = False

        # Si on a appuyé sur une touche du clavier
        elif evenement.type == pygame.KEYDOWN:
            # Si on a appuyé sur la touche Echap (Esc)
            if evenement.key == pygame.K_ESCAPE:
                # On sort de la boucle
                marche = False

    # On récupère les touches actuellement appuyées
    touches = pygame.key.get_pressed()


    # On se sert de variables pour le mouvement
    mouvementX = 0
    mouvementY = 0
 

    # On teste les touches appuyées
    if touches[pygame.K_q]:
        # Le héros se déplacera vers la gauche à sa prochaine update
        mouvementX = -1 * player1.vitesse
        player1.direction = ">"
    elif touches[pygame.K_d]:
        mouvementX = player1.vitesse
        player1.direction = "<"

    if touches[pygame.K_z]:
        mouvementY = -1*player1.vitesse
    elif touches[pygame.K_s]:
        mouvementY = player1.vitesse

    

    # On assigne les variables au tuple de mouvement du héros
    player1.mouvement = (mouvementX, mouvementY)
           
    
    # On demande aux éléments des groupes de se mettre à jour
    player1_groupe.update(tic)
    
    


    # On efface l'écran
    ecran.fill((0, 150, 0))


    # On dessine tous les membres des groupes sur une surface donnée et le score
    player1_groupe.draw(ecran)
    

    pygame.display.update()
    horloge.tick(fps)