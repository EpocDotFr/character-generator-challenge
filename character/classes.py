__all__ = [
    'WarriorCharacterClass',
    'WizardCharacterClass',
    'ThiefCharacterClass'
]


class BaseCharacterClass:
    pass


class WarriorCharacterClass(BaseCharacterClass):
    id = 2
    name = 'Warrior'


class WizardCharacterClass(BaseCharacterClass):
    id = 4
    name = 'Wizard'


class ThiefCharacterClass(BaseCharacterClass):
    id = 8
    name = 'Thief'
