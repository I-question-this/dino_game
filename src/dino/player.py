import pygame
from dino.assets import DINO_DOUX
from dino.spritesheet import SpriteSheet

# TODO: Move constants to seperate file that is imported into each file.
# Color
RED = (255, 0, 0)
BLACK = (0, 0, 0)
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """

    # -- Methods
    def __init__(self, width, height):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # Set double jump
        # ONLY WORKS IF IT HITS A PLATFORM
        # THE BOTTOM PART OF THE SCREEN IS NOT A PLATFORM
        self.double_jump_available = True

        # List of all the frames for the little dino
        # Load the sprite sheet image and extract images; (x, y, width, height)
        sprite_sheet = SpriteSheet(DINO_DOUX, width, height)
        self.frames = []
        for i in range(0, 10):
            # Get the image from the sprite sheet
            image = sprite_sheet.get_image((i*24)+4, 4, 15, 18)
            # Scale the image up
            image = sprite_sheet.transform_image(image)
            # Add the image to the list of frames
            self.frames.append(image)

        # Set direction
        self.direction = 'R' # Faces 'R'ight or 'L'eft

        # Set the image the player starts with
        self.image = self.frames[0]
 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        # Testing
        self.state = 'Idle' # Options Jumping, Walking, Idle
        self.frame_number = 0

        

    def update(self, level):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # First check jumping, then other states.
        if self.change_x != 0: 
            self.state = 'Walking'
        else:
            self.state = 'Idle'

        # Change Direction
        if self.change_x > 0:
            self.direction = 'R'
        elif self.change_x < 0:
            self.direction = 'L'        

        # frame = ((self.rect.x + level.world_shift_x) // 30) % len(self.frames)
        if self.direction is 'R':
            self.image = self.frames[self.frame_number]
        else:
            self.image = pygame.transform.flip(self.frames[self.frame_number], True, False)
        
        print(f'STATE: {self.state}')
        print(f'FRAME: {self.frame_number}')

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, level.block_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
            else:
                self.state = 'Jumping' 

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, level.block_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                # Stop our vertical movement, only when it hits the ground
                self.change_y = 0
                self.double_jump_available = True
            elif self.change_y < 0:
                # Not setting the vertical movement to 0 here lets it be floaty
                self.rect.top = block.rect.bottom

        # Get the correct frame number to display
        # Idle Frames [0:2]
        # Walking Frames [3:11]
        # Jump Frame [0]
        if self.state == 'Jumping':
            self.frame_number = 0
        elif self.state == 'Walking':
            if 1 < self.frame_number < 9:
                self.frame_number += 1
            else:
                self.frame_number = 3
        else:
            if -1 < self.frame_number < 2:
                self.frame_number += 1
            else:
                self.frame_number = 0


    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .45

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self, level):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a block below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a block moving down.
        self.rect.y += 2
        block_hit_list = pygame.sprite.spritecollide(self, level.block_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(block_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
        elif self.double_jump_available:
            self.change_y = -10
            self.double_jump_available = False

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
