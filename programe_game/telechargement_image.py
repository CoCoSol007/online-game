import pygame

pygame.init()

def download(couleur):
    
    if couleur == "red":
        tilset = pygame.image.load("programe_game\Enemi_spite.png")
    elif couleur == "blue":
        tilset = pygame.image.load("programe_game\player_spite.png")
    
    
    
    liste_image = [
        
    
            tilset.subsurface(0*32,0*32,32,32),
            tilset.subsurface(1*32,0*32,32,32),
            tilset.subsurface(2*32,0*32,32,32),
            
        
    ]

    for i in range (0,9):
        liste_image.append(pygame.transform.flip(liste_image[i],True, False))
        
    
        
    return liste_image






