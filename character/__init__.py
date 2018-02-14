from . import abilities
from . import classes
from . import races
import random


class Character:
    """Represents an RPG character."""
    abilities = abilities.CharacterAbilities()

    def __init__(self, name=None, race=None, class_=None):
        self.name = name
        self.race = race
        self.class_ = class_

    def randomize(self):
        self.race = random.choice(races.ALL)()
        self.class_ = random.choice(classes.ALL)()
        self.abilities.randomize_values()
