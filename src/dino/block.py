import pygame


GREEN = (0, 255, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, left, top, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        
