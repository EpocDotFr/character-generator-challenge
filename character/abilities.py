import random

MIN_VALUE = 0
MAX_VALUE = 10


class BaseCharacterAbility:
    """Base character ability to inherit from.

    Minimum value is 0, maximum value is 10."""
    value = MIN_VALUE


class StrengthCharacterAbility(BaseCharacterAbility):
    id = 'strength'
    name = 'Strength'


class ResistanceCharacterAbility(BaseCharacterAbility):
    id = 'resistance'
    name = 'Resistance'


class DexterityCharacterAbility(BaseCharacterAbility):
    id = 'dexterity'
    name = 'Dexterity'


class IntelligenceCharacterAbility(BaseCharacterAbility):
    id = 'intelligence'
    name = 'Intelligence'


ALL = [
    StrengthCharacterAbility,
    ResistanceCharacterAbility,
    DexterityCharacterAbility,
    IntelligenceCharacterAbility
]


class CharacterAbilities:
    """A character's abilities."""

    def __init__(self):
        for ability in ALL:
            setattr(self, ability.id, ability())

    def randomize_values(self):
        """Assign random values to all the abilities."""

        for ability in ALL:
            getattr(self, ability.id).value = random.randint(MIN_VALUE, MAX_VALUE)
