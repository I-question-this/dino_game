import pygame
from dino.assets.sprites.dinos import DINO_BART_FRAMES
from dino.entities.entity import Entity, Direction

# TODO SWITCH DIRECTION NOT JUST WHEN FALLING BUT ALSO WHEN COLLIDING IN X DIR

class Enemy(Entity):
    """ This class represents the bar at the bottom that the player
        controls. """

    def __init__(self, width, height, spawn):
        super().__init__(width, height, spawn, 2, 10)

    def load_spritesheet(self, width, height):
        self.sprite_sheet = DINO_BART_FRAMES(width, height)

    def update(self, level):
        """ Move the Enemy. """
        # Move in direction they're facing
        if self.direction == Direction.LEFT:
            self.go_left()
        else:
            self.go_right()

        super().update(level)

