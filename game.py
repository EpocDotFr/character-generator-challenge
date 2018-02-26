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
import gui


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
        self.character.randomize_all()

        self._load_gui()

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
            },
            'buttons': {
                'exit': helpers.load_image('buttons/exit.png'),
                'randomize': helpers.load_image('buttons/randomize.png'),
                'save': helpers.load_image('buttons/save.png')
            }
        }

    def _load_gui(self):
        """Load the GUI elements (i.e elements the user can interact with)."""
        # Character's race selector
        spacing = 270

        for race in character.races.ALL:
            race_image_rect = self.images['races']['normal'][race.id].get_rect() # We don't care about the type of button rect we take
            race_image_rect.right = spacing
            race_image_rect.top = 76

            gui.add(gui.RadioButton(
                {
                    'normal': self.images['races']['normal'][race.id],
                    'selected': self.images['races']['active'][race.id]
                },
                race_image_rect,
                'race',
                race,
                on_click=self._click_race_button,
                selected=isinstance(self.character.race, race)
            ))

            spacing += 50

        # Randomize character name button
        randomize_name_button_rect = self.images['buttons']['randomize'].get_rect()
        randomize_name_button_rect.top = 35
        randomize_name_button_rect.right = self.window_rect.w - 20

        gui.add(gui.Button(
            self.images['buttons']['randomize'],
            randomize_name_button_rect,
            self._click_randomize_name_button
        ))

        # Randomize all character attributes button
        randomize_all_button_rect = self.images['buttons']['randomize'].get_rect()
        randomize_all_button_rect.bottom = self.window_rect.h - 10
        randomize_all_button_rect.right = self.window_rect.w - 110

        gui.add(gui.Button(
            self.images['buttons']['randomize'],
            randomize_all_button_rect,
            self._click_randomize_all_button
        ))

        # Save the character sheet in a text file button
        save_button_rect = self.images['buttons']['save'].get_rect()
        save_button_rect.bottom = self.window_rect.h - 10
        save_button_rect.right = self.window_rect.w - 60

        gui.add(gui.Button(
            self.images['buttons']['save'],
            save_button_rect,
            self._click_save_button
        ))

        # Exit button
        exit_button_rect = self.images['buttons']['exit'].get_rect()
        exit_button_rect.bottom = self.window_rect.h - 10
        exit_button_rect.right = self.window_rect.w - 10

        gui.add(gui.Button(
            self.images['buttons']['exit'],
            exit_button_rect,
            self._click_exit_button
        ))

    def save_character_sheet(self):
        """Save the current character's sheet in a text file."""
        logging.info('Saving character')

        with open(settings.CHARACTER_SHEET_FILE_NAME, 'w', encoding='utf-8') as f:
            f.write(str(self.character))

    def update(self):
        """Perform every updates of the game logic, events handling and drawing.
        Also known as the game loop."""

        # Events handling
        for event in pygame.event.get():
            event_handlers = [
                self._event_quit,
                gui.event_handler
            ]

            for handler in event_handlers:
                if handler(event):
                    break

        # Drawings
        self.window.blit(self.images['window'], self.images['window'].get_rect())

        self._draw_name_input()
        self._draw_classes_selector()
        self._draw_abilities()
        self._draw_skills()

        gui.draw(self.window)

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

    def _click_exit_button(self, element):
        """Called when the Exit button is clicked."""
        pygame.quit()
        sys.exit()

    def _click_randomize_name_button(self, element):
        """Called when the Randomize character name button is clicked."""
        self.character.randomize_name()

    def _click_randomize_all_button(self, element):
        """Called when the Randomize all character attributes button is clicked."""
        self.character.randomize_all()

    def _click_save_button(self, element):
        """Called when the Save character button is clicked."""
        self.save_character_sheet()

    def _click_race_button(self, element):
        """Called when the user selects a race."""
        self.character.race = element.value()

    # --------------------------------------------------------------------------
    # Drawing handlers

    def _draw_name_input(self):
        """Draw the character's name input."""
        name_text = self.fonts['normal'].render(self.character.name, True, settings.TEXT_COLOR)
        name_text_rect = name_text.get_rect()
        name_text_rect.left = 240
        name_text_rect.top = 43

        self.window.blit(name_text, name_text_rect)

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

            spacing += 30
