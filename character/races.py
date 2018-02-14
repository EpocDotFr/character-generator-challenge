__all__ = [
    'HumanCharacterRace',
    'ElfCharacterRace',
    'DwarfCharacterRace',
    'OrcCharacterRace'
]


class BaseCharacterRace:
    pass


class HumanCharacterRace(BaseCharacterRace):
    id = 2
    name = 'Human'


class ElfCharacterRace(BaseCharacterRace):
    id = 4
    name = 'Elf'


class DwarfCharacterRace(BaseCharacterRace):
    id = 8
    name = 'Dwarf'


class OrcCharacterRace(BaseCharacterRace):
    id = 12
    name = 'Orc'
