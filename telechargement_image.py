import pygame

pygame.init()

def download(couleur):
    
    if couleur == "red":
        tilset = pygame.image.load("PlayerSprite0.png")
    elif couleur == "blue":
        tilset = pygame.image.load("PlayerSprite1.png")
    
    
    
    list_of_grenouille = [
        
    
            tilset.subsurface(0*64,0*64,64,64),
            tilset.subsurface(1*64,0*64,64,64),
            tilset.subsurface(2*64,0*64,64,64),
            tilset.subsurface(3*64,0*64,64,64),
            tilset.subsurface(3*64,0*64,64,64),
            tilset.subsurface(0*64,1*64,64,64),
            tilset.subsurface(1*64,1*64,64,64),
            tilset.subsurface(2*64,1*64,64,64),
            tilset.subsurface(3*64,1*64,64,64),
            
        
    ]

    for i in range (0,9):
        list_of_grenouille.append(pygame.transform.flip(list_of_grenouille[i],True, False))
        
    for image in list_of_grenouille:
        pygame.transform.scale(image, (4000,3000))
        
    return list_of_grenouille






