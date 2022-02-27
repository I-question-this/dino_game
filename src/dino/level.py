import json
import pygame
import random

from dino.blocks.basic import BasicBlock
from dino.blocks.death import DeathBlock
from dino.blocks.invisible import InvisibleBlock
from dino.blocks.moving import MovingBlock
from dino.blocks.spawn import SpawnBlock
from dino.blocks.win import WinBlock
from dino.entities.enemy import Enemy
from dino.entities.player import Player
from dino.constants import BLUE, PLAYER_SYMBOL, BASIC_BLOCK_SYMBOLS,\
                           INVISIBLE_BLOCK_SYMBOL, DEATH_BLOCK_SYMBOL,\
                           ENEMY_SYMBOL, WIN_SYMBOL, MOVING_SYMBOL, \
                           TILE_HEIGHT, TILE_WIDTH, \
                           SCREEN_WIDTH, SCREEN_HEIGHT
from dino.assets import BACKGROUNDS_JUNGLE, BACKGROUNDS_SNOW, BACKGROUNDS_DESERT, BACKGROUNDS_SKY

class Level:
    def __init__(self, view, tile_width, tile_height, map_file, info_file):
        # View information
        self.view = view
        self.world_shift_x = 0
        self.world_shift_y = 0

        # Tile Information
        self.tile_width = tile_width
        self.tile_height = tile_height

        # Load level specific info
        with open(info_file) as fin:
            info = json.load(fin)
            moving_info = info["moving_info"]
        moving_block_index = 0

        # Level Complete
        self.done = False

        # Load level map
        self.block_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.spawn_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()

        with open(map_file) as fin:
            raw_map = fin.read().split("\n")

        # Details for player respawn, and out-of-bounds check
        tile_height_count = len(raw_map)
        tile_width_count = max(len(row) for row in raw_map)
        self.world_size = (tile_width_count * tile_width,
                        tile_height_count * tile_height)
        # This is default, safety value. It should not be used.
        self.player_spawn = SpawnBlock(0, 0, tile_width, tile_height)

        for row in range(len(raw_map)):
            for col in range(len(raw_map[row])):
                # Determine x, y
                x = tile_width * col
                y = tile_height * row
                # Determine tile symbol
                tile_symbol = raw_map[row][col]

                if tile_symbol == PLAYER_SYMBOL:
                    self.player_spawn = SpawnBlock(x, y, 
                                                   tile_width,
                                                   tile_height)
                    self.spawn_list.add(self.player_spawn)
                elif tile_symbol in BASIC_BLOCK_SYMBOLS:
                    self.block_list.add(BasicBlock(x, y, 
                                                   tile_width, tile_height, tile_symbol))
                elif tile_symbol == INVISIBLE_BLOCK_SYMBOL:
                    self.block_list.add(InvisibleBlock(x, y,
                                                       tile_width, tile_height))
                elif tile_symbol == DEATH_BLOCK_SYMBOL:
                    self.block_list.add(DeathBlock(x, y, 
                                                   tile_width, tile_height))
                elif tile_symbol == ENEMY_SYMBOL:
                    spawn = SpawnBlock(x, y, tile_width, tile_height)
                    self.spawn_list.add(spawn)
                    self.enemy_list.add(Enemy(tile_width, tile_height, spawn))
                elif tile_symbol == WIN_SYMBOL:
                    self.block_list.add(WinBlock(x, y,
                                                    tile_width, tile_height, tile_symbol))
                elif tile_symbol == MOVING_SYMBOL:
                    self.block_list.add(
                            MovingBlock(x, y, tile_width, tile_height, 
                                        tile_symbol,
                                        moving_info[moving_block_index]["top"],
                                        moving_info[moving_block_index]["bottom"],
                                        moving_info[moving_block_index]["left"],
                                        moving_info[moving_block_index]["right"],
                                        moving_info[moving_block_index]["change_x"],
                                        moving_info[moving_block_index]["change_y"]
                                        ))
                    moving_block_index += 1
                elif tile_symbol == " ":
                    # Ignore empty spaces
                    pass
                else:
                    raise ValueError(f"Unknown tile symbol: {tile_symbol}")

        # Create player
        self.player = Player(tile_width, tile_height, self.player_spawn)
        self.player_list.add(self.player)

        # Set a theme for the level 
        self.theme = random.choice([BACKGROUNDS_SKY, BACKGROUNDS_DESERT, 
                                        BACKGROUNDS_JUNGLE, BACKGROUNDS_SNOW])
        # Create the background image sequence for the level
        self.background = self.create_background()

    def reset_player(self):
        self.player.revive()

    def reset_enemy(self, enemy):
        enemy.revive()

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        # Update world around the player
        self.block_list.update(self)
        self.enemy_list.update(self)

        # Determine if player has died
        if self.player.dead:
            self.reset_player()

        # Check if player has gone way out of the world
        if abs(self.player.rect.right - self.player_spawn.rect.right)\
                > self.world_size[0]\
            or abs(self.player.rect.top - self.player_spawn.rect.top)\
                > self.world_size[1]:
                self.reset_player()

        # Determine if player has left the world view
        x_diff = 0
        y_diff = 0

        if self.player.rect.right >= self.view.right:
            x_diff = self.view.right - self.player.rect.right
            self.player.rect.right = self.view.right

        if self.player.rect.left <= self.view.left:
            x_diff = self.view.left - self.player.rect.left
            self.player.rect.left = self.view.left

        if self.player.rect.top <= self.view.top:
            y_diff = self.view.top - self.player.rect.top
            self.player.rect.top = self.view.top

        if self.player.rect.bottom >= self.view.bottom:
            y_diff = self.view.bottom - self.player.rect.bottom
            self.player.rect.bottom = self.view.bottom

        self.shift_world(x_diff, y_diff)

        # Update the player
        self.player.update(self)

    # Shift everything but the player in this world
    def shift_world(self, x_diff, y_diff):
        self.world_shift_x += x_diff
        self.world_shift_y += y_diff

        # Go through all the sprite lists and shift
        for spawn in self.spawn_list:
            spawn.rect.x += x_diff
            spawn.rect.y += y_diff

        for block in self.block_list:
            block.rect.x += x_diff
            block.rect.y += y_diff

        for enemy in self.enemy_list:
            enemy.rect.x += x_diff
            enemy.rect.y += y_diff

    def draw(self, screen):
        """ Draw everything on this level. """
        # Draw the background
        self.draw_background(screen)

        # Draw all the sprite lists that we have
        self.block_list.draw(screen)
        self.enemy_list.draw(screen)
        self.player_list.draw(screen)

    def draw_background(self, screen):
        # Copy the sprites from the sequence onto the screen
        screen.blits(self.background)

    def create_background(self):
        # Create a new blank image
        images = [pygame.image.load(self.theme[x]).convert_alpha() for x in range(len(self.theme))]
        images =  [pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT)) for image in images]
 
        rows = (SCREEN_WIDTH // TILE_WIDTH) + 1
        cols = (SCREEN_HEIGHT // TILE_HEIGHT) + 1
        # Create blits sequence
        blit_list = []
        for row in range(0, rows):
            for col in range(0, cols):
                blit_list.append([random.choice(images), (48*row, 48*col)])
        return blit_list