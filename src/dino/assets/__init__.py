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
}

DIRT_BLOCK_FILES = [os.path.join(SPRITES_DIR, "Tiles/tile_0002.png"),
    os.path.join(SPRITES_DIR, "Tiles/tile_0005.png"),
    os.path.join(SPRITES_DIR, "Tiles/tile_0024.png"),
    os.path.join(SPRITES_DIR, "Tiles/tile_0025.png"),
]