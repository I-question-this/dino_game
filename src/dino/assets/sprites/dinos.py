from functools import partial
from dino.assets import DINO_DOUX, DINO_BART, DINO_MORT, DINO_VITA
from dino.assets.sprites.spritesheet import SpriteSheet

class DinoSpriteSheet(SpriteSheet):
    def _prepare_frames(self):
        self.frames = []
        for i in range(10):
            # Get the image from the sprite sheet
            image = self._get_image((i*24)+4, 4, 15, 18)
            # Scale the image up
            image = self._transform_image(image)
            # Add the image to the list of frames
            self.frames.append(image)

DINO_DOUX_FRAMES = partial(DinoSpriteSheet, DINO_DOUX, 3, 7)
DINO_BART_FRAMES = partial(DinoSpriteSheet, DINO_BART, 3, 7)
DINO_MORT_FRAMES = partial(DinoSpriteSheet, DINO_MORT, 3, 7)
DINO_VITA_FRAMES = partial(DinoSpriteSheet, DINO_VITA, 3, 7)
