from faker import Faker
from . import abilities
from . import classes
from . import races
import faker.config
import locale


class Character:
    """Represents an RPG character."""
    abilities = abilities.CharacterAbilities()

    def __init__(self, name=None, race=None, class_=None):
        self.name = name
        self.race = race
        self.class_ = class_

    def randomize(self):
        default_locale = locale.getdefaultlocale()[0]
        fake = Faker(default_locale if default_locale in faker.config.AVAILABLE_LOCALES else faker.config.DEFAULT_LOCALE)

        self.name = fake.first_name_male()
        self.race = races.pick_random()
        self.class_ = classes.pick_random()
        self.abilities.randomize()
