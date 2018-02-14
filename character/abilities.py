__all__ = [
    'CharacterAbilities'
]


class BaseAbility:
    value = 0


class StrenghtAbility(BaseAbility):
    id = 2
    name = 'Strength'


class ResistanceAbility(BaseAbility):
    id = 4
    name = 'Resistance'


class DexterityAbility(BaseAbility):
    id = 8
    name = 'Dexterity'


class IntelligenceAbility(BaseAbility):
    id = 12
    name = 'Intelligence'


class CharacterAbilities:
    strenght = StrenghtAbility()
    resistance = ResistanceAbility()
    dexterity = DexterityAbility()
    intelligence = IntelligenceAbility()
