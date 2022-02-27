from abc import ABC, abstractmethod
from enum import Enum, auto
import pygame

from dino.assets import DINO_DOUX
from dino.blocks.death import DeathBlock


class Direction(Enum):
    RIGHT = auto()
    LEFT = auto()


class State(Enum):
    IDLE = auto()
    WALKING = auto()


class Entity(pygame.sprite.Sprite, ABC):
    """ This class represents the bar at the bottom that the player
        controls. """

    # -- Methods
    def __init__(self, width, height, spawn, speed, jump_speed):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set death status
        self.dead = False

        # Save spawn point
        self.spawn = spawn

        # Set speed vector of entity
        self.change_x = 0
        self.change_y = 0
        self.speed = speed
        self.jump_speed = jump_speed

        # Set double jump
        self.double_jump_available = True

        # Load sprite sheet
        self.load_spritesheet(width, height)
        # load frames
        self.frames = self.sprite_sheet.frames

        # Set initial values
        self.revive()

    @abstractmethod
    def load_spritesheet(self, width, height):
        ...

    def revive(self):
        # Set direction
        self.direction = Direction.RIGHT

        # Set the image the player starts with
        self.image = self.frames[0]
 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        # Set location
        self.rect.left = self.spawn.rect.left
        self.rect.top = self.spawn.rect.top

        # Set animation state
        self.state = State.IDLE
        self.frame_number = 0

        # Set status values
        self.dead = False
        self.double_jump_available = True


    def update(self, level):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # Change Direction
        if self.change_x > 0:
            self.direction = Direction.RIGHT
        elif self.change_x < 0:
            self.direction = Direction.LEFT        

        # See if we hit anything
        x_axis_block_hit_list = pygame.sprite.spritecollide(self, 
                level.block_list, False)
        for block in x_axis_block_hit_list:
            if isinstance(block, DeathBlock):
                self.dead = True

            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        y_axis_block_hit_list = pygame.sprite.spritecollide(self, 
                level.block_list, False)
        for block in y_axis_block_hit_list:
            if isinstance(block, DeathBlock):
                self.dead = True

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                # Stop our vertical movement, only when it hits the ground
                self.change_y = 0
                self.double_jump_available = True
            elif self.change_y < 0:
                # Not setting the vertical movement to 0 here lets it be floaty
                self.change_y = 0
                self.rect.top = block.rect.bottom

        # First check jumping, then other states.
        if self.change_x != 0: 
            self.state = State.WALKING
        else:
            self.state = State.IDLE

        # Get the correct frame number to display
        # Idle Frames [0:2]
        # Walking Frames [3:11]
        self.frame_number += 3
        if self.frame_number > 240:
            self.frame_number = 0
        if self.state == State.WALKING:
            # walk_frames = self.frames[3:11]
            walk_frames = self.frames[3:]
            frame = (((self.rect.x + level.world_shift_x + self.frame_number) // 30) % len(walk_frames)) + 3
        else:
            frame = self.frame_number // 80
            

        if self.direction is Direction.RIGHT:
            self.image = self.frames[frame]
        else:
            self.image = pygame.transform.flip(self.frames[frame], True, False)

        return x_axis_block_hit_list, y_axis_block_hit_list

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .5

    def jump(self, level):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a block below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a block moving down.
        self.rect.y += 2
        block_hit_list = pygame.sprite.spritecollide(self, level.block_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(block_hit_list) > 0:
            self.change_y = -self.jump_speed
        elif self.double_jump_available:
            self.change_y = -self.jump_speed
            self.double_jump_available = False

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -self.speed

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = self.speed

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
