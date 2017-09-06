from random import shuffle, randint
from copy import deepcopy

from homework1 import stable_marriage as sm


class Person:
    def __init__(self, name):
        self.preference_list = []
        self.name = name
        self.partner = None

    def __str__(self):
        return "{0} {1}".format(self.name, self.partner)

    def __repr__(self):
        return "{0} {1}".format(self.name, self.partner)


class Man(Person):
    def __init__(self, name):
        Person.__init__(self, name)


class Woman(Person):
    def __init__(self, name):
        Person.__init__(self, name)


class Game:
    def __init__(self):
        pass

    @staticmethod
    def create_players(men, women, mens_names, womens_names):
        while womens_names and mens_names:
            women.append(sm.Woman(womens_names.pop(randint(0, len(womens_names) - 1))))
            men.append(sm.Man(mens_names.pop(randint(0, len(mens_names) - 1))))

    @staticmethod
    def set_preferences(men, women, mens_names, womens_names):
        for m, w in zip(men, women):
            shuffle([womens_names])
            m.preference_list = deepcopy(womens_names)
            shuffle([mens_names])
            w.preference_list = deepcopy(mens_names)

    def gale_shapley(self, men, women):
        for m, w in zip(men, women):
            pass
