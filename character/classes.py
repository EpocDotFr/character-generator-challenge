import random


class BaseCharacterClass:
    """Base character class to inherit from."""
    def __str__(self):
        """Return this class as a textual representation."""
        return self.name


class WarriorCharacterClass(BaseCharacterClass):
    id = 'warrior'
    name = 'Warrior'


class WizardCharacterClass(BaseCharacterClass):
    id = 'wizard'
    name = 'Wizard'


class ThiefCharacterClass(BaseCharacterClass):
    id = 'thief'
    name = 'Thief'


ALL = [
    WarriorCharacterClass,
    WizardCharacterClass,
    ThiefCharacterClass
]


def pick_random():
    """Return a random class."""
    return random.choice(ALL)
