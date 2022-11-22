import sys

import pygame

from settings import Settings

# Be yourself, everyone else is already taken
class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Don't get caught!
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # Liz, please put some text in a comment here.


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Sometimes I'll just stand here for hours watching tv.

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible. This process of drawing and flipping reduces flicker.
            pygame.display.flip()

# The application starts here.
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    # Zach, please put some text in a comment here.
    ai.run_game()
