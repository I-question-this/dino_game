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

        x_axis_player_hit_list = pygame.sprite.spritecollide(self, 
                level.player_list, False)

        for player in x_axis_player_hit_list:
            if self.change_x > 0:
                self.rect.right = player.rect.left
                self.direction = Direction.LEFT
                player.dead = True
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = player.rect.right    
                self.direction = Direction.RIGHT
                player.dead = True

        x_axis_enemy_hit_list = pygame.sprite.spritecollide(self, 
                level.enemy_list, False)

        for enemy in x_axis_enemy_hit_list:
            if enemy is not self:
                if self.change_x > 0:
                    self.rect.right = enemy.rect.left
                    self.direction = Direction.LEFT
                elif self.change_x < 0:
                    # Otherwise if we are moving left, do the opposite.
                    self.rect.left = enemy.rect.right    
                    self.direction = Direction.RIGHT

        y_axis_player_hit_list = pygame.sprite.spritecollide(self, 
                level.player_list, False)

        for player in y_axis_player_hit_list:
            if self.change_y > 0:
                self.rect.bottom = player.rect.top
                # Stop our vertical movement, only when it hits the ground
                self.change_y = 0
                player.dead = True
            elif self.change_y < 0:
                # Not setting the vertical movement to 0 here lets it be floaty
                self.change_y = 0
                self.rect.top = player.rect.bottom   
                player.dead = True

        if len(x_axis_block_hit_list) > 0:
            if self.direction == Direction.LEFT:
                self.direction = Direction.RIGHT
            else:
                self.direction = Direction.LEFT

