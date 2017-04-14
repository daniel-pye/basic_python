import random
from combat import Combat

COLOURS = ['yellow', 'red', 'blue', 'green', 'purple']


class Monster(Combat):
    min_hitpoints = 1
    max_hitpoints = 1000
    min_experience = 1
    max_experience = 1000
    weapon = 'sword'
    sound = 'shout'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hitpoints, self.max_hitpoints)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.colour = random.choice(COLOURS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} {}, HP: {} XP: {}'.format(self.colour.title(), self.__class__.__name__, self.hit_points, self.experience)

    def battlecry(self):
        return self.sound.upper()


class Goblin(Monster):
    max_hitpoints = 3
    max_experience = 2
    sound = 'scream'


class Troll(Monster):
    min_hitpoints = 3
    max_hitpoints = 5
    min_experience = 2
    max_experience = 6
    sound = 'growl'


class Dragon(Monster):
    min_hitpoints = 10
    max_hitpoints = 30
    min_experience = 10
    max_experience = 30
    sound = 'roar'
