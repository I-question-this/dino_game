import pygame
BLUE = (0, 0, 255)

class World:
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, boundry):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.boundry = boundry

        self.world_shift_x = 0
        self.world_shift_y = 0

    # Update everything on this level
    def update(self, player):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

        x_diff = 0
        y_diff = 0

        # Determine if player has left the world view boundary
        if player.rect.right >= self.boundry.right:
            x_diff = self.boundry.right - player.rect.right
            player.rect.right = self.boundry.right

        if player.rect.left <= self.boundry.left:
            x_diff = self.boundry.left - player.rect.left
            player.rect.left = self.boundry.left

        if player.rect.top <= self.boundry.top:
            y_diff = self.boundry.top - player.rect.top
            player.rect.top = self.boundry.top

        if player.rect.bottom >= self.boundry.bottom:
            y_diff = self.boundry.bottom - player.rect.bottom
            player.rect.bottom = self.boundry.bottom

        self.shift_world(x_diff, y_diff)

    def shift_world(self, x_diff, y_diff):
        self.world_shift_x += x_diff
        self.world_shift_y += y_diff

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += x_diff
            platform.rect.y += y_diff

        for enemy in self.enemy_list:
            enemy.rect.x += x_diff
            enemy.rect.x += y_diff

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(BLUE)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
