"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

From:
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py

Explanation video: http://youtu.be/BCxWJgN4Nnc

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""

from queue import Empty
from xml.dom.minicompat import EmptyNodeList
import pygame

from dino.assets import LEVEL_1_INFO, LEVEL_1_MAP, LEVEL_2_INFO, LEVEL_2_MAP
from dino.level import Level
from dino.constants import SCREEN_WIDTH, SCREEN_HEIGHT, VIEW_RECT,\
                           TILE_WIDTH, TILE_HEIGHT

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer Jumper")

    # Create all the levels
    level_list = []
    level_list.append(Level(VIEW_RECT, TILE_WIDTH, TILE_HEIGHT, 
                            LEVEL_1_MAP, LEVEL_1_INFO))
    level_list.append(Level(VIEW_RECT, TILE_WIDTH, TILE_HEIGHT, 
                            LEVEL_2_MAP, LEVEL_2_INFO))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_level.player.go_left()
                if event.key == pygame.K_RIGHT:
                    current_level.player.go_right()
                if event.key == pygame.K_UP:
                    current_level.player.jump(current_level)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT\
                        and current_level.player.change_x < 0:
                    current_level.player.stop()
                if event.key == pygame.K_RIGHT\
                        and current_level.player.change_x > 0:
                    current_level.player.stop()

        # Update the level
        current_level.update()
        if current_level.done:
            current_level_no += 1
            if current_level_no >= len(level_list):
                done = True
            else:
                current_level = level_list[current_level_no]

        # Draw the level
        current_level.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
