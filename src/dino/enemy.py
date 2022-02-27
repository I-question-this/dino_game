import pygame
from dino.assets import DINO_BART
from dino.spritesheet import SpriteSheet

# TODO SWITCH DIRECTION NOT JUST WHEN FALLING BUT ALSO WHEN COLLIDING IN X DIR

class Enemy(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """

    # -- Methods
    def __init__(self, width, height, x, y):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()

        # Set Spawn coordinate reminder
        self.spawn_x = x
        self.spawn_y = y

        # Set speed vector of enemy
        self.change_x = 0
        self.change_y = 0

        # List of all the frames for the little dino
        # Load the sprite sheet image and extract images; (x, y, width, height)
        sprite_sheet = SpriteSheet(DINO_BART, width, height)
        self.frames = []
        for i in range(3, 10):
            # Get the image from the sprite sheet 
            image = sprite_sheet.get_image((i*24)+4, 4, 15, 18)
            # Scale the image up
            image = sprite_sheet.transform_image(image)
            # Add the image to the list of frames
            self.frames.append(image)

        # Set direction
        self.direction = 'L' # Faces 'R'ight or 'L'eft

        # Set the image the player starts with
        self.image = self.frames[0]
 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        # Set player state to determine which frames to play
        self.state = 'Idle' # Options: Walking, Idle
        self.frame_number = 0

    def update(self, level, player):
        """ Move the Enemy. """
        # Gravity
        self.calc_grav()

        # Move in direction they're facing
        if self.direction == 'L':
            self.go_left()
        else:
            self.go_right()
        
        block_hit_list = pygame.sprite.spritecollide(self, level.block_list, False)
        # Check and see if we would walk off the box
        for block in block_hit_list:
            if (self.rect.x + self.change_x > block.rect.right) or (self.rect.x + self.change_x < block.rect.left):
                # Enemy would walk off the side of the box. Turn around
                self.change_x = -self.change_x

        # Change Direction
        if self.change_x > 0:
            self.direction = 'R'
        elif self.change_x < 0:
            self.direction = 'L'   
        
        # Move left/right
        self.rect.x += self.change_x     

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
            elif self.change_y < 0:
                # Not setting the vertical movement to 0 here lets it be floaty
                self.change_y = 0
                self.rect.top = block.rect.bottom

        # Get correct frame and display
        frame = (((self.rect.x + level.world_shift_x) // 30) % len(self.frames))
        if self.direction is 'R':
            self.image = self.frames[frame]
        else:
            self.image = pygame.transform.flip(self.frames[frame], True, False)

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .5
    
    # Automatic Movement
    def go_left(self):
        """ Called during update when the enemy is facing left"""
        self.change_x = -2

    def go_right(self):
        """ Called during update when the enemy is facing right"""
        self.change_x = 2
