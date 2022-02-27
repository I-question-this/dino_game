import pygame
from dino.assets.sprites.dinos import DINO_DOUX_FRAMES
from dino.entities.entity import Entity
from dino.blocks.win import WinBlock


class Player(Entity):
    """ This class represents the bar at the bottom that the player
        controls. """
    def __init__(self, width, height, spawn):
        super().__init__(width, height, spawn, 6, 10, 8)

    def load_spritesheet(self, width, height):
        self.sprite_sheet = DINO_DOUX_FRAMES(width, height)

    
    def update(self, level):
        x_axis_block_hit_list, y_axis_block_hit_list = super().update(level)
        for block in x_axis_block_hit_list:
            if isinstance(block, WinBlock):
                level.done = True
        for block in y_axis_block_hit_list:
            if isinstance(block, WinBlock):
                level.done = True


        x_axis_enemy_hit_list = pygame.sprite.spritecollide(self, 
                level.enemy_list, False)

        for enemy in x_axis_enemy_hit_list:
            if self.change_x > 0:
                self.rect.right = enemy.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = enemy.rect.right        
            self.dead = True

        y_axis_enemy_hit_list = pygame.sprite.spritecollide(self, 
                level.enemy_list, False)

        for enemy in y_axis_enemy_hit_list:
            if self.change_y > 0:
                self.rect.bottom = enemy.rect.top
                # Stop our vertical movement, only when it hits the ground
                self.change_y = 0
            elif self.change_y < 0:
                # Not setting the vertical movement to 0 here lets it be floaty
                self.change_y = 0
                self.rect.top = enemy.rect.bottom
            self.dead = True

        