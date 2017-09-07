from copy import copy
from random import shuffle, randint

from homework1 import stable_marriage as sm


class Person:
    def __init__(self, name):
        self.preference_list = []
        self.preference_list_copy = []
        self.name = name
        self.partner = None

    def __str__(self):
        if self.partner:
            return "{0} {1}".format(self.name, self.partner.name)
        else:
            return "{0} {1}".format(self.name, "None")

    def __repr__(self):
        if self.partner:
            return "{0} {1}".format(self.name, self.partner.name)
        else:
            return "{0} {1}".format(self.name, "None")


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
    def set_preferences(men, women, size):
        nums = [i for i in range(size)]
        for m, w in zip(men, women):
            shuffle(nums)
            for n in nums:
                m.preference_list.append(women[n])
                w.preference_list.append(men[n])
            m.preference_list_copy = copy(m.preference_list)
            w.preference_list_copy = copy(w.preference_list)

    @staticmethod
    def gale_shapley(men):
        # choose man not yet married
        single_men = copy(men)
        while single_men:
            m = single_men.pop(0)
            # choose woman on man's list with highest rating
            while m.preference_list and not m.partner:
                w = m.preference_list.pop(0)
                if not w.partner:
                    m.partner = w
                    w.partner = m
                else:
                    proposed_partner_rating = w.preference_list.index(m)
                    current_partner_rating = w.preference_list.index(w.partner)
                    # If woman prefers the suggested partner over her current partner,
                    # then make her partner the suggested partner
                    if current_partner_rating > proposed_partner_rating:
                        m.partner = w
                        w.partner.partner = None
                        single_men.append(w.partner)
                        w.partner = m
