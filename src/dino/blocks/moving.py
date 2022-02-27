import pygame
from dino.blocks.basic import BasicBlock

class MovingBlock(BasicBlock):
    def __init__(self, left, top, width, height, block, boundary_top,
                 boundary_bottom, boundary_left, boundary_right, change_x, 
                 change_y):
        super().__init__(left, top, width, height, block)

        self.boundary_top = self.rect.top - height * boundary_top
        self.boundary_bottom = self.rect.bottom + height * boundary_bottom
        self.boundary_left = self.rect.left - width * boundary_left
        self.boundary_right = self.rect.right + width * boundary_right

        self.change_x = change_x
        self.change_y = change_y
    
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

        # Check if player is on top
        self.rect.y -= 2
        hit = pygame.sprite.collide_rect(self, level.player)
        self.rect.y += 2
        if hit:
            level.player.rect.x += self.change_x
            level.player.rect.y += self.change_y

        # Check the boundaries and see if we need to reverse
        # direction.
        cur_y = self.rect.y - level.world_shift_y
        if  cur_y < self.boundary_top or cur_y > self.boundary_bottom:
            self.change_y *= -1

        cur_x = self.rect.x - level.world_shift_x
        if  cur_x < self.boundary_left or cur_x > self.boundary_right:
            self.change_x *= -1

