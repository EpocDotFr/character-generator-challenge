from . import abilities
from . import classes


class BaseCharacterSkill:
    """Base skill to inherit from."""
    applicable_classes = []
    required_abilities = {}


class ThiefCharacterSkill(BaseCharacterSkill):
    applicable_classes = [
        classes.ThiefCharacterClass
    ]


class WarriorCharacterSkill(BaseCharacterSkill):
    applicable_classes = [
        classes.WarriorCharacterClass
    ]


class WizardCharacterSkill(BaseCharacterSkill):
    applicable_classes = [
        classes.WizardCharacterClass
    ]


class StealthCharacterSkill(ThiefCharacterSkill):
    id = 'stealth'
    name = 'Stealth'

    required_abilities = {
        abilities.IntelligenceCharacterAbility: 2
    }


class PicklockCharacterSkill(ThiefCharacterSkill):
    id = 'picklock'
    name = 'Picklock'

    required_abilities = {
        abilities.DexterityCharacterAbility: 3
    }


class HighKickCharacterSkill(WarriorCharacterSkill):
    id = 'high_kick'
    name = 'High-kick'

    required_abilities = {
        abilities.StrengthCharacterAbility: 2
    }


class RunnerCharacterSkill(WarriorCharacterSkill):
    id = 'runner'
    name = 'Runner'

    required_abilities = {
        abilities.StrengthCharacterAbility: 3
    }


class MagicalHealCharacterSkill(WizardCharacterSkill):
    id = 'magical_heal'
    name = 'Magical Heal'

    required_abilities = {
        abilities.IntelligenceCharacterAbility: 2
    }


class FireballCharacterSkill(WizardCharacterSkill):
    id = 'fireball'
    name = 'Fireball'

    required_abilities = {
        abilities.IntelligenceCharacterAbility: 3
    }


ALL = [
    StealthCharacterSkill,
    PicklockCharacterSkill,
    HighKickCharacterSkill,
    RunnerCharacterSkill,
    MagicalHealCharacterSkill,
    FireballCharacterSkill
]
