from abc import ABC, abstractmethod
import pygame 

from dino.constants import BLACK

class SpriteSheet(ABC):
    """ Class used to grab images out of a sprite sheet. """
 
    def __init__(self, file_name, walk_frames_start, num_walk_frames,
                 entity_width, entity_height):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Save widths/heights
        self.entity_width = entity_width
        self.entity_height = entity_height

        # Save frame information
        self.walk_frames_start = walk_frames_start
        self.num_walk_frames = num_walk_frames

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

        # Load the frames
        self._prepare_frames()

    @abstractmethod
    def _prepare_frames(self):
        ...
 
    def _get_image(self, x, y, width, height):
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


    def _transform_image(self, image):
        image = pygame.transform.scale(image, 
                                       (self.entity_width, self.entity_height))
        return image

