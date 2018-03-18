from random import randint, choice


class NameGenerator(object):
    """Random fantasy name generator.

    From http://sametmax.com/generateur-de-nom-dheroic-fantasy-en-python/, adapted to Python 3."""
    VOWELS = (
        (('start', 'middle', 'end'), (
                (5, ("a", "e", "i", "o", "u")),
                (1, ("ae", "ai", "ao", "au", "aa", "ea", "eo", "eu", "ee", "ia",
                     "io", "iu", "ii", "oa", "oe", "oi", "ou", "oo", "eau", "y"))
        )),
        (('middle'), (
            (1, ("'",)),
        ))
    )

    CONSONANTS = (
        (('start', 'middle', 'end'), (
                (3, ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p",
                     "r", "s", "t", "v", "w")),
                (1, ("x", "y", "z", "sc", "ch", "gh", "ph", "sh", "th", "sk", "wk", "st"))
        )),
        (('middle', 'end'), (
                (1, ("ck", "nk", "rk", "ss")),
        )),
        (('start', 'middle'), (
                (2, ("br", "dr", "fr", "gr", "kr", )),
                (1, ("cr", "pr", "sr", "tr", "qu", "wh", "cl", "fl", "gl", "kl",
                     "ll", "pl", "sl", "str"))
        )),
    )

    SYLLABLES_POOL = [[], []]

    for i, group in enumerate((VOWELS, CONSONANTS)):
        pool = SYLLABLES_POOL[i]
        for place, pack in group:
            for frequency, letters in pack:
                for letter in letters:
                    pool.extend(((letter, set(place)),) * frequency)

    def __init__(self, min_syllable=2, max_syllable=None):
        self.min_syllable = min_syllable
        self.max_syllable = max_syllable or (min_syllable + 2)

    def get_new_name(self):
        return self.generate_name(self.min_syllable, self.max_syllable)

    @classmethod
    def generate_name(cls, min_syllable, max_syllable, base=""):
        length, pool = randint(min_syllable, max_syllable), randint(0, 1)

        for i in range(1, length + 1):
            while True:

                letter, place = choice(cls.SYLLABLES_POOL[pool])

                if i == 1:
                    if 'start' not in place:
                        continue
                elif i == length:
                    if 'end' not in place:
                        continue
                else:
                    if 'middle' not in place:
                        continue

                base += letter
                pool = abs(pool - 1)
                break

        return base.title()
