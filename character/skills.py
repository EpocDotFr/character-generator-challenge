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


class FightCharacterSkill(BaseCharacterSkill):
    id = 'fight'
    name = 'Fight'

    applicable_classes = [
        classes.WarriorCharacterClass
    ]
