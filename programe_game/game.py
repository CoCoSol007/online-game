import pygame
from programe_game.Entity import *
from programe_game.bullet import bullet

pygame.init()

def main(conexion, path):
    
    # On créé une horloge (pour les FPS)
    horloge = pygame.time.Clock()


    # On créé un écran pour notre programme (= une fenêtre)
    screen = pygame.display.set_mode( (800, 600) )
    fond = pygame.image.load("programe_game\screen.png")
    fond = pygame.transform.scale(fond, (800,600))

    # On définit le taux de rafraîchissement de la fenêtre
    fps = 30



    # On instancie un héros
    player = Player(conexion)
    enemi = Enemi(conexion)

    object_to_draw = pygame.sprite.Group(player, enemi)



    # On créé un groupe où placer le héros
    player_groupe = pygame.sprite.Group()

    # On ajoute le héros au groupe
    player_groupe.add(player)

    Tic_animation = 0
    tic_bullet = 0
    Bullet_remain = True

    # On créé une variable pour sortir de la boucle principale
    marche = True

    # On met en place la boucle principale d'affichage
    while marche:
        
        Tic_animation += 0.25
        tic_bullet += 1
        if Tic_animation == 4:
            Tic_animation = 0
        if tic_bullet  == 50:
            Bullet_remain = True
            tic_bullet = 0

        
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
            if Bullet_remain: 
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    player.shoot = 1
                    object_to_draw.add(bullet(player))
                    Bullet_remain = False 


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
        object_to_draw.update(Tic_animation)
        enemi.group.update(Tic_animation)
        
        # On efface l'écran
        screen.blit(fond, (0,0))
        

        # On dessine tous les membres des groupes sur une surface donnée et le score
        object_to_draw.draw(screen)
        enemi.group.draw(screen)
        

        pygame.display.update()
        horloge.tick(fps)


import threading

def creer_un_thread( cible):

	thread = threading.Thread(target=cible)
	thread.daemon = True
	thread.start()