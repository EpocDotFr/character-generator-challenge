from character import Character
import settings
import logging
import helpers
import pygame
import sys


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(settings.WINDOW_SIZE, pygame.DOUBLEBUF)
        self.window_rect = self.window.get_rect()

        pygame.display.set_caption('Character Generator')
        pygame.display.set_icon(helpers.load_image('icon.png'))

        self._load_fonts()
        self._load_images()

        self._start_new_game()

    def _load_fonts(self):
        """Load the fonts."""
        logging.info('Loading fonts')

        self.fonts = {
            # TODO
        }

    def _load_images(self):
        """Load all images."""
        logging.info('Loading images')

        self.images = {
            # TODO
        }

    def _start_new_game(self):
        """Start a new game."""
        logging.info('Initializing new game')

        self.character = Character()
        self.character.randomize()

        # TODO

    def update(self):
        """Perform every updates of the game logic, events handling and drawing.
        Also known as the game loop."""

        # Events handling
        for event in pygame.event.get():
            event_handlers = [
                self._event_quit
                # TODO
            ]

            for handler in event_handlers:
                if handler(event):
                    break

        # Drawings
        # TODO

        # PyGame-related updates
        pygame.display.update()

        self.clock.tick(settings.FPS)

    # --------------------------------------------------------------------------
    # Events handlers

    def _event_quit(self, event):
        """Called when the game must be closed."""
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        return False

    # --------------------------------------------------------------------------
    # Drawing handlers

    # TODO
