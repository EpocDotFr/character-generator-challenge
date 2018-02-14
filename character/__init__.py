from . import abilities
from . import classes
from . import races


class Character:
    def __init__(self, name, race=races.HumanCharacterRace(), class_=classes.WarriorCharacterClass()):
        self.name = name
        self.race = race
        self.class_ = class_
        self.abilities = abilities.CharacterAbilities()
