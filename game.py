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
        self.save_character_sheet()

    def _load_fonts(self):
        """Load the fonts."""
        logging.info('Loading fonts')

        self.fonts = {
            'normal': helpers.load_font('celtic_gaelige.ttf', 21)
        }

    def _load_images(self):
        """Load all images."""
        logging.info('Loading images')

        self.images = {
            'window': helpers.load_image('window.png'),
            'abilities': {ability.id: helpers.load_image('abilities/' + ability.id + '.png') for ability in character.abilities.ALL},
            'skills': {skill.id: helpers.load_image('skills/' + skill.id + '.png') for skill in character.skills.ALL},
            'races': {
                'normal': {race.id: helpers.load_image('races/' + race.id + '.png') for race in character.races.ALL},
                'active': {race.id: helpers.load_image('races/' + race.id + '_active.png') for race in character.races.ALL}
            },
            'classes': {
                'normal': {class_.id: helpers.load_image('classes/' + class_.id + '.png') for class_ in character.classes.ALL},
                'active': {class_.id: helpers.load_image('classes/' + class_.id + '_active.png') for class_ in character.classes.ALL}
            }
        }

    def save_character_sheet(self):
        """Save the current character's sheet in a Markdown-formatted file."""
        logging.info('Saving character')

        with open(settings.CHARACTER_SHEET_FILE_NAME, 'w', encoding='utf-8') as f:
            f.write(str(self.character))

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

        self._draw_name_input()
        self._draw_races_selector()
        self._draw_classes_selector()
        self._draw_abilities()
        self._draw_skills()

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

    def _draw_name_input(self):
        """Draw the character's name input."""
        name_text = self.fonts['normal'].render(self.character.name, True, settings.TEXT_COLOR)
        name_text_rect = name_text.get_rect()
        name_text_rect.left = 240
        name_text_rect.top = 43

        self.window.blit(name_text, name_text_rect)

    def _draw_races_selector(self):
        """Draw images to choose the character's race."""
        spacing = 270

        for race in character.races.ALL:
            race_image = self.images['races']['active' if isinstance(self.character.race, race) else 'normal'][race.id]
            race_image_rect = race_image.get_rect()
            race_image_rect.right = spacing
            race_image_rect.top = 76

            self.window.blit(race_image, race_image_rect)

            spacing += 50

    def _draw_classes_selector(self):
        """Draw images to choose the character's class."""
        spacing = 270

        for class_ in character.classes.ALL:
            class_image = self.images['classes']['active' if isinstance(self.character.class_, class_) else 'normal'][class_.id]
            class_image_rect = class_image.get_rect()
            class_image_rect.right = spacing
            class_image_rect.top = 116

            self.window.blit(class_image, class_image_rect)

            spacing += 50

    def _draw_abilities(self):
        """Draw the character's abilities."""
        spacing = 235

        for ability in character.abilities.ALL:
            ability_image = self.images['abilities'][ability.id]
            ability_image_rect = ability_image.get_rect()
            ability_image_rect.left = 25
            ability_image_rect.top = spacing

            self.window.blit(ability_image, ability_image_rect)

            ability_text = self.fonts['normal'].render(ability.name, True, settings.TEXT_COLOR)
            ability_text_rect = ability_text.get_rect()
            ability_text_rect.left = 55
            ability_text_rect.top = spacing

            self.window.blit(ability_text, ability_text_rect)

            ability_value = self.fonts['normal'].render(str(getattr(self.character.abilities, ability.id).value), True, settings.TEXT_COLOR)
            ability_value_rect = ability_value.get_rect()
            ability_value_rect.left = 210
            ability_value_rect.top = spacing

            self.window.blit(ability_value, ability_value_rect)

            spacing += 30

    def _draw_skills(self):
        """Draw the character's skills."""
        spacing = 235

        for skill in self.character.skills:
            skill_image = self.images['skills'][skill.id]
            skill_image_rect = skill_image.get_rect()
            skill_image_rect.left = 265
            skill_image_rect.top = spacing

            self.window.blit(skill_image, skill_image_rect)

            skill_text = self.fonts['normal'].render(skill.name, True, settings.TEXT_COLOR)
            skill_text_rect = skill_text.get_rect()
            skill_text_rect.left = 295
            skill_text_rect.top = spacing

            self.window.blit(skill_text, skill_text_rect)

            spacing += 28
