from copy import deepcopy
from random import shuffle, randint

from homework1 import stable_marriage as sm


class Person:
    def __init__(self, name):
        self.preference_list = []
        # self.preferences_map = {}
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
            shuffle(womens_names)
            shuffle(mens_names)
            m.preference_list = deepcopy(mens_names)
            w.preference_list = deepcopy(womens_names)
            # for i, (mn, wn) in enumerate(zip(mens_names, womens_names)):
            #     m.preferences_map[wn] = i
            #     w.preferences_map[mn] = i

    @staticmethod
    def gale_shapley(men):
        free_men = deepcopy(men)
        while free_men:
            m = free_men[0]
            while m.preference_list:
                w = m.preference_list.pop(0)
                if not w.partner:
                    m.partner = w
                    w.partner = m
                else:
                    m_rating = w.preferences_[m.name]
                    m_prime_rating = w.preferences_list[w.partner]
                    if m_prime_rating < m_rating:
                        m.partner = w
                        w.partner = m
                        free_men.pop(0)
                        free_men.append(w.partner)
