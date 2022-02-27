import pygame
from dino.assets.sprites.dinos import DINO_DOUX_FRAMES
from dino.entities.entity import Entity


class Player(Entity):
    """ This class represents the bar at the bottom that the player
        controls. """
    def __init__(self, width, height, spawn):
        super().__init__(width, height, spawn, 6, 10)

    def load_spritesheet(self, width, height):
        self.sprite_sheet = DINO_DOUX_FRAMES(width, height)
