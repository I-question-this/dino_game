import pygame
from dino.blocks.basic import BasicBlock

class MovingBlock(BasicBlock):
    def __init__(self, left, top, width, height, block):
        super().__init__(left, top, width, height, block)

        self.change_x = 1
        self.change_y = 1

        self.boundary_top = self.rect.top - height * 4
        self.boundary_bottom = self.rect.bottom + height * 4
        self.boundary_left = self.rect.left - width * 4
        self.boundary_right = self.rect.right + width * 4

        print(f"Top: {self.rect.top} -- {self.boundary_top}")
        print(f"Bottom: {self.rect.bottom} -- {self.boundary_bottom}")
        print(f"Left: {self.rect.left} -- {self.boundary_left}")
        print(f"Right: {self.rect.right} -- {self.boundary_right}")


    
    def update(self, level):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, level.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                level.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                level.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, level.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                level.player.rect.bottom = self.rect.top
            else:
                level.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        cur_pos_y = self.rect.y - level.world_shift_y
        if cur_pos_y > self.boundary_bottom or cur_pos_y < self.boundary_top:
            self.change_y *= -1

        cur_pos_x = self.rect.x - level.world_shift_x
        if cur_pos_x < self.boundary_left or cur_pos_x > self.boundary_right:
            self.change_x *= -1
