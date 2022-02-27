import pygame
from dino.blocks.basic import BasicBlock

class WinBlock(BasicBlock):
    def __init__(self, left, top, width, height, block):
        super().__init__(left, top, width, height, block)
