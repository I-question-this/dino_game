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
VIEW_WIDTH = 700
VIEW_HEIGHT = 500
VIEW_RECT = pygame.Rect((SCREEN_WIDTH-VIEW_WIDTH)//2,
                            (SCREEN_HEIGHT-VIEW_HEIGHT)//2,
                            VIEW_WIDTH, VIEW_HEIGHT)

# Tile Size
TILE_WIDTH = 48
TILE_HEIGHT = 48

# Tile Symbols
PLAYER_SYMBOL = "P"
BLOCK_SYMBOL = "B"
