import pygame
from dino.assets import DINO_DOUX


# TODO: Move constants to seperate file that is imported into each file.
# TODO: Move SpriteSheet
# Color
RED = (255, 0, 0)
BLACK = (0, 0, 0)
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class SpriteSheetOld():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha() # Convert alpha gives per-pixel transparancy to png images
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        return image

class SpriteSheet():
    """ Class used to grab images out of a sprite sheet. """
 
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
 
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()
 
 
    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
 
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Assuming black works as the transparent color
        image.set_colorkey(BLACK)
 
        # Return the image
        return image


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 40
        height = 60

        """
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        """
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # Set double jump
        # ONLY WORKS IF IT HITS A PLATFORM
        # THE BOTTOM PART OF THE SCREEN IS NOT A PLATFORM
        self.double_jump_available = True

        # List of sprites we can bump against
        self.level = None

        # List of all the frames for the little dino
        # Load the sprite sheet image and extract images
        sprite_sheet = SpriteSheet(DINO_DOUX)
        self.frames = [sprite_sheet.get_image(0, 0, 24, 24),
                sprite_sheet.get_image(24, 0, 24, 24)]
        self.frame_number = 0

        # Set the image the player starts with
        self.image = self.frames[0]
 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()


    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
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
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
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

        frame = (self.rect.x // 30) % len(self.frames)
        self.image = self.frames[frame]

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

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
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