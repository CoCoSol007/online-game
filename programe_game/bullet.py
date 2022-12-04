import pygame

class bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()

        self.player = player

        self.image = pygame.image.load("programe_game\Bullet.png")

        if self.player.type == "player":
            self.image = self.image.subsurface(0*8,0*8,8,8)

        else :
            self.image = self.image.subsurface(1*8,0*8,8,8)

        self.image = pygame .transform.scale(self.image, (32,32))

        self.rect = self.image.get_rect()

        self.rect.center = self.player.rect.center
        self.dirction = self.player.direction

        self.speed = 20

    def update(self, tic):

        if self.dirction == ">":
            self.rect.centerx -= self.speed
        else : self.rect.centerx += self.speed


        if self.rect.centerx < 0 or self.rect.centerx > 800:
            self.kill()

    