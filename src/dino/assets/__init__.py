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
LEVEL_2_INFO = os.path.join(LEVEL_DIR, "level_2.json")
LEVEL_2_MAP = os.path.join(LEVEL_DIR, "level_2.lvl")
LEVEL_3_INFO = os.path.join(LEVEL_DIR, "level_3.json")
LEVEL_3_MAP = os.path.join(LEVEL_DIR, "level_3.lvl")

# Tile Files
BASIC_BLOCK_FILES = {
    "T":os.path.join(SPRITES_DIR, "Tiles/tile_0022.png"),
    "R":os.path.join(SPRITES_DIR, "Tiles/tile_0023.png"),
    "G":os.path.join(SPRITES_DIR, "Tiles/tile_0000.png"),
    "l":os.path.join(SPRITES_DIR, "Tiles/tile_0001.png"),
    "g":os.path.join(SPRITES_DIR, "Tiles/tile_0002.png"),
    "r":os.path.join(SPRITES_DIR, "Tiles/tile_0003.png"),
    "B":os.path.join(SPRITES_DIR, "Tiles/tile_0006.png"),
    "t":os.path.join(SPRITES_DIR, "Tiles/tile_0020.png"),
    "L":os.path.join(SPRITES_DIR, "Tiles/tile_0021.png"),
    "O":os.path.join(SPRITES_DIR, "Tiles/tile_0142.png"),
    "n":os.path.join(SPRITES_DIR, "Tiles/tile_0143.png"),
    "N":os.path.join(SPRITES_DIR, "Tiles/tile_0141.png"),
    "q":os.path.join(SPRITES_DIR, "Tiles/tile_0121.png"),
    "Q":os.path.join(SPRITES_DIR, "Tiles/tile_0123.png"),
    "o":os.path.join(SPRITES_DIR, "Tiles/tile_0120.png"),
    "W":os.path.join(SPRITES_DIR, "Tiles/tile_0130.png"),
    "M":os.path.join(SPRITES_DIR, "Tiles/tile_0047.png")
}

DIRT_BLOCK_FILES = [
    os.path.join(SPRITES_DIR, "Tiles/tile_0122.png")
]

BACKGROUNDS_SKY = [
    os.path.join(SPRITES_DIR, "Backgrounds/background_0000.png"),
    os.path.join(SPRITES_DIR, "Backgrounds/background_0001.png"),
    os.path.join(SPRITES_DIR, "Backgrounds/background_0002.png"),
]

BACKGROUNDS_DESERT = [    
    os.path.join(SPRITES_DIR, "Backgrounds/background_0003.png"),
    os.path.join(SPRITES_DIR, "Backgrounds/background_0004.png"),
    os.path.join(SPRITES_DIR, "Backgrounds/background_0005.png")
]

BACKGROUNDS_SNOW = [
    os.path.join(SPRITES_DIR, "Backgrounds/background_0006.png"),
    os.path.join(SPRITES_DIR, "Backgrounds/background_0007.png"),
    os.path.join(SPRITES_DIR, "Backgrounds/background_0008.png"),
]

BACKGROUNDS_JUNGLE = [    
    os.path.join(SPRITES_DIR, "Backgrounds/background_0009.png"),
    os.path.join(SPRITES_DIR, "Backgrounds/background_0010.png"),
    os.path.join(SPRITES_DIR, "Backgrounds/background_0011.png")
]
