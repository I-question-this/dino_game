import pygame
from dino.assets.sprites.dinos import DINO_BART_FRAMES
from dino.entities.entity import Entity, Direction


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

        x_axis_block_hit_list, y_axis_block_hit_list = super().update(level)

        if len(x_axis_block_hit_list) > 0:
            if self.direction == Direction.LEFT:
                self.direction = Direction.RIGHT
            else:
                self.direction = Direction.LEFT

