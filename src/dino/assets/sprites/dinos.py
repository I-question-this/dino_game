from functools import partial
from dino.assets import DINO_DOUX, DINO_BART, DINO_MORT, DINO_VITA
from dino.assets.sprites.spritesheet import SpriteSheet
class DinoSpriteSheet(SpriteSheet):
    def __init__(self, file_name, 
                 entity_width, entity_height):
        super().__init__(file_name=file_name,
                         walk_frames_start = 3,
                         num_walk_frames=7,
                         death_frames_start=14,
                         num_death_frames=3,
                         entity_width=entity_width,
                         entity_height=entity_height)

    def _prepare_frames(self):
        self.frames = []
        for i in range(20):
            # Get the image from the sprite sheet
            image = self._get_image((i*24)+4, 4, 15, 18)
            # Scale the image up
            image = self._transform_image(image)
            # Add the image to the list of frames
            self.frames.append(image)
                            

DINO_DOUX_FRAMES = partial(DinoSpriteSheet, DINO_DOUX)
DINO_BART_FRAMES = partial(DinoSpriteSheet, DINO_BART)
DINO_MORT_FRAMES = partial(DinoSpriteSheet, DINO_MORT)
DINO_VITA_FRAMES = partial(DinoSpriteSheet, DINO_VITA)
