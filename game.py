from character import Character
import character.abilities
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

        self.character = Character()
        self.character.randomize()

    def _load_fonts(self):
        """Load the fonts."""
        logging.info('Loading fonts')

        self.fonts = {
            'normal': helpers.load_font('celtic_gaelige.ttf', 22),
        }

    def _load_images(self):
        """Load all images."""
        logging.info('Loading images')

        self.images = {
            # TODO
        }

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
        self.window.fill(settings.WINDOW_BACKGROUND_COLOR)

        self._draw_general_attributes_panel()
        self._draw_abilities_attributes_panel()

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

    def _draw_general_attributes_panel(self):
        name_text = self.fonts['normal'].render('Name', True, settings.TEXT_COLOR)
        name_text_rect = name_text.get_rect()
        name_text_rect.left = 40
        name_text_rect.top = 20

        self.window.blit(name_text, name_text_rect)

        race_text = self.fonts['normal'].render('Race', True, settings.TEXT_COLOR)
        race_text_rect = race_text.get_rect()
        race_text_rect.left = 40
        race_text_rect.top = name_text_rect.bottom + 20

        self.window.blit(race_text, race_text_rect)

        class_text = self.fonts['normal'].render('Class', True, settings.TEXT_COLOR)
        class_text_rect = class_text.get_rect()
        class_text_rect.left = 40
        class_text_rect.top = race_text_rect.bottom + 20

        self.window.blit(class_text, class_text_rect)

    def _draw_abilities_attributes_panel(self):
        abilities_text = self.fonts['normal'].render('Abilities', True, settings.TEXT_COLOR)
        abilities_text_rect = abilities_text.get_rect()
        abilities_text_rect.left = 20
        abilities_text_rect.top = 150

        self.window.blit(abilities_text, abilities_text_rect)

        spacing = abilities_text_rect.bottom + 20

        for ability in character.abilities.ALL:
            ability_text = self.fonts['normal'].render(ability.name, True, settings.TEXT_COLOR)
            ability_text_rect = ability_text.get_rect()
            ability_text_rect.left = 40
            ability_text_rect.top = spacing

            self.window.blit(ability_text, ability_text_rect)

            ability_value = self.fonts['normal'].render(str(ability.value), True, settings.TEXT_COLOR)
            ability_value_rect = ability_value.get_rect()
            ability_value_rect.left = 180
            ability_value_rect.top = spacing

            self.window.blit(ability_value, ability_value_rect)

            spacing += 40
