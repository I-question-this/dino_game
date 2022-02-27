import pygame
import random
from dino.assets import BASIC_BLOCK_FILES, DIRT_BLOCK_FILES

class BasicBlock(pygame.sprite.Sprite):
    def __init__(self, left, top, width, height, block):
        super().__init__()
        if block == "b":
            # Borderless dirt block. Choose randomly from the dirt block files
            file_name = random.choice(DIRT_BLOCK_FILES)
        else:
            # Block has a specific border. Get file of block type
            file_name = BASIC_BLOCK_FILES[block]
        image = pygame.image.load(file_name).convert_alpha()
        self.image = pygame.transform.scale(image, (width, height))

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
