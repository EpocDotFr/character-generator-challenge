class BaseCharacterRace:
    """Base character race to inherit from."""
    pass


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
