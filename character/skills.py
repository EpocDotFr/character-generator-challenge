from . import classes


class BaseSkill:
    pass


class StealthSkill(BaseSkill):
    id = 2
    name = 'Stealth'

    applicable_classes = [
        classes.ThiefCharacterClass
    ]


class FightSkill(BaseSkill):
    id = 4
    name = 'Fight'

    applicable_classes = [
        classes.WarriorCharacterClass
    ]
