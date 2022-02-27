import pygame

class InvisibleBlock(pygame.sprite.Sprite):
    def __init__(self, left, top, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height]).convert()
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.image.set_alpha(0)
        
