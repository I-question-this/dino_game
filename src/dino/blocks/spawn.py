import pygame

from dino.blocks.invisible import InvisibleBlock

class SpawnBlock(InvisibleBlock):
    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)
