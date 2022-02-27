import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
VIEW_WIDTH = 400
VIEW_HEIGHT = 300
VIEW_RECT = pygame.Rect((SCREEN_WIDTH-VIEW_WIDTH)//2,
                            (SCREEN_HEIGHT-VIEW_HEIGHT)//2,
                            VIEW_WIDTH, VIEW_HEIGHT)

# Tile Size
TILE_WIDTH = 48
TILE_HEIGHT = 48

# Tile Symbols
PLAYER_SYMBOL = "P"
INVISIBLE_BLOCK_SYMBOL = "I"
DEATH_BLOCK_SYMBOL = "D"
ENEMY_SYMBOLS = ["E", "e"]
WIN_SYMBOL = "W"
MOVING_SYMBOL = "M"
BASIC_BLOCK_SYMBOLS = ["T", "R", "G", "l", "g", "r", "B", "t", "L", "b", "O", "o", "N", "n", "q", "Q"]
