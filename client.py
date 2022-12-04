# On importe le module pygame
import pygame
from Entity import *
import threading
import socket

def creer_un_thread( cible):

		thread = threading.Thread(target=cible)
		thread.daemon = True
		thread.start()

connexion = socket.socket()
host = '192.168.1.40'
port = 2004
connexion.connect((host, port))
envoi("join", connexion)


        

# On initialise pygame
pygame.init()

# On créé une horloge (pour les FPS)
horloge = pygame.time.Clock()




# On créé un écran pour notre programme (= une fenêtre)
screen = pygame.display.set_mode( (800, 600) )
fond = pygame.image.load("screen.png")
fond = pygame.transform.scale(fond, (800,600))

# On définit le taux de rafraîchissement de la fenêtre
fps = 30



# On instancie un héros
player = Player(connexion)
enemi = Enemi(connexion)

object_to_draw = pygame.sprite.Group(player, enemi)



# On créé un groupe où placer le héros
player_groupe = pygame.sprite.Group()

# On ajoute le héros au groupe
player_groupe.add(player)

tic = 0

# On créé une variable pour sortir de la boucle principale
marche = True

# On met en place la boucle principale d'affichage
while marche:
    
    tic += 0.25
    if tic == 4:
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
        # Multiplying the value of `player.vitesse` by -1 and assigning the result to `mouvementX`.
        mouvementX = -1 * player.vitesse
        player.direction = ">"
    elif touches[pygame.K_d]:
        # Assigning the value of `player.vitesse` to `mouvementX`.
        mouvementX = player.vitesse
        player.direction = "<"

    if touches[pygame.K_z]:
        mouvementY = -1*player.vitesse
    elif touches[pygame.K_s]:
        mouvementY = player.vitesse

    

    # Assigning the values of `mouvementX` and `mouvementY` to the `mouvement` attribute of `player`.
    player.mouvement = (mouvementX, mouvementY)
           

    #on recupere la position de l'enemie
    creer_un_thread(cible= enemi.recevoir_donnees)
    
    # On demande aux éléments des groupes de se mettre à jour
    object_to_draw.update(tic)
    
    
    
    


    # On efface l'écran
    screen.blit(fond, (0,0))
    

    # On dessine tous les membres des groupes sur une surface donnée et le score
    object_to_draw.draw(screen)
    

    pygame.display.update()
    horloge.tick(fps)

envoi("stop", connexion)