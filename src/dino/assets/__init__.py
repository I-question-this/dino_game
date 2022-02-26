"""Assets directory"""

__author__="Tyler Westland"

import os

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
SPRITES_DIR = os.path.join(ASSETS_DIR, "sprites")

DINO_DOUX = os.path.join(SPRITES_DIR, "DinoSprites--doux.png")
DINO_BART = os.path.join(SPRITES_DIR, "DinoSprites--bart.png")
DINO_MORT = os.path.join(SPRITES_DIR, "DinoSprites--mort.png")
DINO_VITA = os.path.join(SPRITES_DIR, "DinoSprites--vita.png")

LEVEL_DIR = os.path.join(ASSETS_DIR, "levels")
LEVEL_1_INFO = os.path.join(LEVEL_DIR, "level_1.json")
LEVEL_1_MAP = os.path.join(LEVEL_DIR, "level_1.lvl")
