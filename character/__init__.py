from faker import Faker
from . import abilities
from . import classes
from . import skills
from . import races
import faker.config
import locale


default_locale = locale.getdefaultlocale()[0]
fake = Faker(default_locale if default_locale in faker.config.AVAILABLE_LOCALES else faker.config.DEFAULT_LOCALE)


class Character:
    """Represents an RPG character."""
    abilities = abilities.CharacterAbilities()
    skills = []

    def __init__(self, name=None, race=None, class_=None):
        self.name = name
        self.race = race
        self.class_ = class_

    @property
    def class_(self):
        return self.class__

    @class_.setter
    def class_(self, value):
        self.class__ = value

        self.update_applicable_skills()

    def randomize_all(self):
        """Randomize this character's attributes."""
        self.abilities.randomize()
        self.name = fake.first_name_male()
        self.race = races.pick_random()()
        self.class_ = classes.pick_random()()

    def randomize_name(self):
        """Sets a randome name this this character."""
        self.name = fake.first_name_male()

    def update_applicable_skills(self):
        """Set this players's skills according to its class and abilities score."""
        self.skills = []

        for skill in skills.ALL:
            cont = True

            for class_ in skill.applicable_classes:
                if isinstance(self.class_, class_):
                    cont = False

                    break

            if cont:
                continue

            cont = False

            for required_ability, min_value in skill.required_abilities.items():
                if getattr(self.abilities, required_ability.id).value < min_value:
                    cont = True

                    break

            if cont:
                continue

            self.skills.append(skill)

    def __str__(self):
        """Return this character as a textual, Markdown-formatted representation."""
        content = [
            '# Character sheet',
            '',
            '  - Name: ' + self.name,
            '  - Race: ' + str(self.race),
            '  - Class: ' + str(self.class_),
            '',
            '## Abilities',
            ''
        ]

        for ability in abilities.ALL:
            content.append('  - ' + ability.name + ': ' + str(getattr(self.abilities, ability.id).value))

        content.extend([
            '',
            '## Skills',
            ''
        ])

        if not self.skills:
            content.append('None applicable.')
        else:
            for skill in self.skills:
                content.append('  - ' + skill.name)

        return '\n'.join(content)
