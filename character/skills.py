from . import classes


class BaseCharacterSkill:
    """Base skill to inherit from."""
    applicable_classes = []


class StealthCharacterSkill(BaseCharacterSkill):
    id = 'stealth'
    name = 'Stealth'

    applicable_classes = [
        classes.ThiefCharacterClass
    ]


class RangedWeaponsCharacterSkill(BaseCharacterSkill):
    id = 'ranged_weapons'
    name = 'Ranged weapons'

    applicable_classes = [
        classes.ThiefCharacterClass
    ]


class CloseCombatCharacterSkill(BaseCharacterSkill):
    id = 'close_combat'
    name = 'Close combat'

    applicable_classes = [
        classes.WarriorCharacterClass
    ]


class AtleticsCharacterSkill(BaseCharacterSkill):
    id = 'Atletics'
    name = 'Atletics'

    applicable_classes = [
        classes.WarriorCharacterClass
    ]
