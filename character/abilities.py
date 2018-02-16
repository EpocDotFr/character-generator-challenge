import random


class BaseCharacterAbility:
    """Base character ability to inherit from."""
    value = 0


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

    def randomize(self):
        """Assign random values to all abilities."""

        for ability in ALL:
            getattr(self, ability.id).value = random.randint(0, 4) # TODO Enhance
