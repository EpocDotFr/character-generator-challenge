from character import Character
import character.abilities
import character.classes
import character.skills
import character.races
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
            'normal': helpers.load_font('celtic_gaelige.ttf', 22)
        }

    def _load_images(self):
        """Load all images."""
        logging.info('Loading images')

        self.images = {
            'window': helpers.load_image('window.png'),
            'abilities': {},
            'skills': {},
            'races': {},
            'classes': {}
        }

        for race in character.races.ALL:
            self.images['races'][race.id] = helpers.load_image('races/' + race.id + '.png')

        for class_ in character.classes.ALL:
            self.images['classes'][class_.id] = helpers.load_image('classes/' + class_.id + '.png')

        for ability in character.abilities.ALL:
            self.images['abilities'][ability.id] = helpers.load_image('abilities/' + ability.id + '.png')

        for skill in character.skills.ALL:
            self.images['skills'][skill.id] = helpers.load_image('skills/' + skill.id + '.png')

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
        self.window.blit(self.images['window'], self.images['window'].get_rect())

        self._draw_races_selector()
        self._draw_classes_selector()
        self._draw_abilities()

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

    def _draw_races_selector(self):
        spacing = 250

        for race in character.races.ALL:
            race_image = self.images['races'][race.id]
            race_image_rect = race_image.get_rect()
            race_image_rect.right = spacing
            race_image_rect.top = 60

            self.window.blit(race_image, race_image_rect)

            spacing += 50

    def _draw_classes_selector(self):
        spacing = 250

        for class_ in character.classes.ALL:
            class_image = self.images['classes'][class_.id]
            class_image_rect = class_image.get_rect()
            class_image_rect.right = spacing
            class_image_rect.top = 100

            self.window.blit(class_image, class_image_rect)

            spacing += 50

    def _draw_abilities(self):
        spacing = 200

        for ability in character.abilities.ALL:
            ability_image = self.images['abilities'][ability.id]
            ability_image_rect = ability_image.get_rect()
            ability_image_rect.left = 20
            ability_image_rect.top = spacing

            self.window.blit(ability_image, ability_image_rect)

            ability_text = self.fonts['normal'].render(ability.name, True, settings.TEXT_COLOR)
            ability_text_rect = ability_text.get_rect()
            ability_text_rect.left = 50
            ability_text_rect.top = spacing

            self.window.blit(ability_text, ability_text_rect)

            ability_value = self.fonts['normal'].render(str(ability.value), True, settings.TEXT_COLOR)
            ability_value_rect = ability_value.get_rect()
            ability_value_rect.left = 210
            ability_value_rect.top = spacing

            self.window.blit(ability_value, ability_value_rect)

            spacing += 28
