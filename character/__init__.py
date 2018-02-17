from faker import Faker
from . import abilities
from . import classes
from . import skills
from . import races
import faker.config
import locale


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

    def randomize(self):
        """Randomize this character's attributes."""
        default_locale = locale.getdefaultlocale()[0]
        fake = Faker(default_locale if default_locale in faker.config.AVAILABLE_LOCALES else faker.config.DEFAULT_LOCALE)

        self.abilities.randomize()
        self.name = fake.first_name_male()
        self.race = races.pick_random()
        self.class_ = classes.pick_random()

    def update_applicable_skills(self):
        """Set this players's skills according to its class and abilities score."""
        self.skills = []

        for skill in skills.ALL:
            if self.class_ not in skill.applicable_classes:
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
        """Return this character as a textual, Markdown representation."""
        content = [
            '# Character cheet',
            '',
            '  - **Name:** ' + self.name,
            '  - **Race:** ' + str(self.race),
            '  - **Class:** ' + str(self.class_),
            '',
            '## Abilities',
            ''
        ]

        for ability in abilities.ALL:
            content.append('  - **' + ability.name + ':** ' + str(getattr(self.abilities, ability.id).value))

        content.extend([
            '',
            '## Skills',
            ''
        ])

        for skill in self.skills:
            content.append('  - ' + skill.name)

        return '\n'.join(content)
