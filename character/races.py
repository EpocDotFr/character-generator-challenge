import random


class BaseCharacterRace:
    """Base character race to inherit from."""
    def __str__(self):
        """Return this race as a textual representation."""
        return self.name


class HumanCharacterRace(BaseCharacterRace):
    id = 'human'
    name = 'Human'


class ElfCharacterRace(BaseCharacterRace):
    id = 'elf'
    name = 'Elf'


class DwarfCharacterRace(BaseCharacterRace):
    id = 'dwarf'
    name = 'Dwarf'


class OrcCharacterRace(BaseCharacterRace):
    id = 'orc'
    name = 'Orc'


ALL = [
    HumanCharacterRace,
    ElfCharacterRace,
    DwarfCharacterRace,
    OrcCharacterRace
]


def pick_random():
    """Return a random race."""
    return random.choice(ALL)
