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

        self.update_applicable_skills()

    def randomize(self):
        """Randomize this character's attributes."""
        default_locale = locale.getdefaultlocale()[0]
        fake = Faker(default_locale if default_locale in faker.config.AVAILABLE_LOCALES else faker.config.DEFAULT_LOCALE)

        self.name = fake.first_name_male()
        self.race = races.pick_random()
        self.class_ = classes.pick_random()
        self.abilities.randomize()

        self.update_applicable_skills()

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
