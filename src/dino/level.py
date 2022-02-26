import json
import pygame

from dino.blocks.basic import BasicBlock
from dino.blocks.death import DeathBlock
from dino.blocks.invisible import InvisibleBlock
from dino.blocks.player_spawn import PlayerSpawnBlock
from dino.constants import BLUE, PLAYER_SYMBOL, BASIC_BLOCK_SYMBOL,\
                           INVISIBLE_BLOCK_SYMBOL, DEATH_BLOCK_SYMBOL


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
            self.boundary_death = info["boundary_death"]

        # Load level map
        self.block_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()

        with open(map_file) as fin:
            raw_map = fin.read().split("\n")

        tile_height_count = len(raw_map)
        tile_width_count = max(len(row) for row in raw_map)
        world_center = (tile_width_count * tile_width,
                        tile_height_count * tile_height)
        self.player_spawn = self.player_spawn = PlayerSpawnBlock(0, 0, 
                                                                 tile_width,
                                                                 tile_height)

        for row in range(len(raw_map)):
            for col in range(len(raw_map[row])):
                # Determine x, y
                x = tile_width * col
                y = tile_height * row
                # Determine tile symbol
                tile_symbol = raw_map[row][col]

                if tile_symbol == PLAYER_SYMBOL:
                    self.player_spawn = PlayerSpawnBlock(x, y, 
                                                         tile_width,
                                                         tile_height)
                elif tile_symbol == BASIC_BLOCK_SYMBOL:
                    self.block_list.add(BasicBlock(x, y, 
                                                   tile_width, tile_height))
                elif tile_symbol == INVISIBLE_BLOCK_SYMBOL:
                    self.block_list.add(InvisibleBlock(x, y,
                                                       tile_width, tile_height))
                elif tile_symbol == DEATH_BLOCK_SYMBOL:
                    self.block_list.add(DeathBlock(x, y, 
                                                   tile_width, tile_height))
                elif tile_symbol == " ":
                    # Ignore empty spaces
                    pass
                else:
                    raise ValueError(f"Unknown tile symbol: {tile_symbol}")


    def reset_player(self, player):
        player.rect.left = self.player_spawn.rect.left
        player.rect.top = self.player_spawn.rect.top
        player.revive()
        self.world_shift_x = 0
        self.world_shift_y = 0


    # Update everything on this level
    def update(self, player):
        """ Update everything in this level."""
        # Update world around the player
        self.block_list.update(player)
        self.enemy_list.update()

        # Determine if player has died
        if player.dead:
            self.reset_player(player)

        # Determine if player has left the world view
        x_diff = 0
        y_diff = 0

        if player.rect.right >= self.view.right:
            x_diff = self.view.right - player.rect.right
            player.rect.right = self.view.right

        if player.rect.left <= self.view.left:
            x_diff = self.view.left - player.rect.left
            player.rect.left = self.view.left

        if player.rect.top <= self.view.top:
            y_diff = self.view.top - player.rect.top
            player.rect.top = self.view.top

        if player.rect.bottom >= self.view.bottom:
            y_diff = self.view.bottom - player.rect.bottom
            player.rect.bottom = self.view.bottom

        self.shift_world(x_diff, y_diff)

    # Shift everything but the player in this world
    def shift_world(self, x_diff, y_diff):
        self.world_shift_x += x_diff
        self.world_shift_y += y_diff

        # Go through all the sprite lists and shift
        self.player_spawn.rect.x += x_diff
        self.player_spawn.rect.y += y_diff

        for block in self.block_list:
            block.rect.x += x_diff
            block.rect.y += y_diff

        for enemy in self.enemy_list:
            enemy.rect.x += x_diff
            enemy.rect.x += y_diff

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(BLUE)

        # Draw all the sprite lists that we have
        self.block_list.draw(screen)
        self.enemy_list.draw(screen)
