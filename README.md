# Character Generator Challenge

My participation to the [PyGame](http://www.pygame.org/) challenge "[Character Generator](https://www.reddit.com/r/pygame/comments/7w8c4j/challenge_character_generator/)"
where the goal is to create a character generation GUI for an RPG-like game.

> TODO Screenshot

## Features

  - Name your character or generate a random one (randomization is based on your current OS locale)
  - Choose you character's race (Human, Elf, Dwarf or Orc) and class (Warrior, Wizard or Thief)
  - Ability scores (Strength, Resistance, Dexterity and Intelligence) are randomly generated
  - Skills are defined based on class and ability scores (minimum required score). Available ones are:
    - Lock Spy (Thief)
    - Stealth (Thief; Intelligence: 2)
    - Picklock (Thief; Intelligence: 3)
    - High-kick (Warrior; Strength: 2)
    - Runner (Warrior; Strength: 3)
    - Earthquake (Warrior; Strength: 4)
    - Magical Heal (Wizard; Intelligence: 2)
    - Fireball (Wizard; Intelligence: 3)
    - Dragon Bite (Wizard; Intelligence: 4)
  - Live preview of your character
  - Ability to randomize everything
  - Save you character's sheet as a Markdown file

## Prerequisites

Python 3. May eventually works with Python 2 (not tested).

## Installation

Clone this repo, and then the usual `pip install -r requirements.txt`.

## Usage

```
python run.py
```

### How it works

I obviously can't explain how it works here, so you'll have to jump yourself in the source code. Start with the entry
point, `run.py`.

## References

  - [Character race](https://en.wikipedia.org/wiki/Character_race) (Wikipedia)
  - [Character class](https://en.wikipedia.org/wiki/Character_class) (Wikipedia)
  - [Attribute (role-playing games)](https://en.wikipedia.org/wiki/Attribute_(role-playing_games)) (Wikipedia)
  - [Statistic (role-playing games): Skills](https://en.wikipedia.org/wiki/Statistic_(role-playing_games)#Skills) (Wikipedia)

## Credits

  - App icon by [Alpár-Etele Méder](https://www.iconfinder.com/icons/1531891/hat_witch_icon) (freeware)
  - Font by [Susan K. Zalusky](https://www.dafont.com/celtic-gaelige.font) (freeware)
  - UI graphics by [Kenney](http://kenney.nl/assets/ui-pack-rpg-expansion) (CC0 1.0 Universal)
  - Game icons by [Game-icons.net](http://game-icons.net/) (several contributors) (CC BY 3.0)
