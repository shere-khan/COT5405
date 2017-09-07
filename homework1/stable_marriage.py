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


man_a = Man('a')
man_j = Man('j')
man_d = Man('d')
man_g = Man('g')
man_t = Man('t')
man_m = Man('m')

woman_t = Woman('t')
woman_f = Woman('f')
woman_ka = Woman('ka')
woman_s = Woman('s')
woman_j = Woman('j')
woman_ky = Woman('ky')


class Game:
    def __init__(self):
        pass

    @staticmethod
    def print_info(men, women):
        # print lists
        for m in men:
            print(m, end=' [')
            for w in m.preference_list_copy:
                print(w.name, end=", ")
            print(']')

        print()
        for w in women:
            print(w, end=' [')
            for m in w.preference_list_copy:
                print(m.name, end=", ")
            print(']')

    @staticmethod
    def create_players(men, women, mens_names, womens_names):
        while womens_names and mens_names:
            women.append(sm.Woman(womens_names.pop(randint(0, len(womens_names) - 1))))
            men.append(sm.Man(mens_names.pop(randint(0, len(mens_names) - 1))))

    @staticmethod
    def create_players_hard(men, women):
        men.append(man_d)
        men.append(man_g)
        men.append(man_a)
        men.append(man_m)
        men.append(man_j)
        men.append(man_t)

        women.append(woman_ka)
        women.append(woman_s)
        women.append(woman_t)
        women.append(woman_ky)
        women.append(woman_f)
        women.append(woman_j)

    @staticmethod
    def set_preferences_hard(men, women):
        men[0].preference_list = [woman_t, woman_f, woman_ka, woman_s, woman_j, woman_ky]
        men[0].preference_list_copy = copy(men[0].preference_list)
        men[1].preference_list = [woman_j, woman_ky, woman_f, woman_ka, woman_s, woman_t]
        men[1].preference_list_copy = copy(men[1].preference_list)
        men[2].preference_list = [woman_j, woman_ka, woman_t, woman_s, woman_ky, woman_f]
        men[2].preference_list_copy = copy(men[2].preference_list)
        men[3].preference_list = [woman_ky, woman_t, woman_j, woman_s, woman_ka, woman_f]
        men[3].preference_list_copy = copy(men[3].preference_list)
        men[4].preference_list = [woman_j, woman_ka, woman_ky, woman_f, woman_s, woman_t]
        men[4].preference_list_copy = copy(men[4].preference_list)
        men[5].preference_list = [woman_ky, woman_t, woman_f, woman_ka, woman_s, woman_j]
        men[5].preference_list_copy = copy(men[5].preference_list)

        women[0].preference_list = [man_a, man_j, man_d, man_g, man_t, man_m]
        women[0].preference_list_copy = copy(women[0].preference_list)
        women[1].preference_list = [man_t, man_m, man_j, man_d, man_g, man_a]
        women[1].preference_list_copy = copy(women[1].preference_list)
        women[2].preference_list = [man_t, man_d, man_a, man_g, man_m, man_j]
        women[2].preference_list_copy = copy(women[2].preference_list)
        women[3].preference_list = [man_m, man_a, man_t, man_g, man_d, man_j]
        women[3].preference_list_copy = copy(women[3].preference_list)
        women[4].preference_list = [man_t, man_d, man_m, man_j, man_g, man_a]
        women[4].preference_list_copy = copy(women[4].preference_list)
        women[5].preference_list = [man_m, man_a, man_j, man_d, man_g, man_t]
        women[5].preference_list_copy = copy(women[5].preference_list)

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
                # w doesn't have a partner
                if not w.partner:
                    m.partner = w
                    w.partner = m
                else:
                    proposed_partner_rating = w.preference_list.index(m)
                    current_partner_rating = w.preference_list.index(w.partner)
                    # If woman prefers m over her current partner,
                    # then make her partner m
                    if current_partner_rating > proposed_partner_rating:
                        # Set m_primes partner to be none and add him back
                        # to the list of single men
                        m_prime = w.partner
                        m_prime.partner = None
                        single_men.append(m_prime)

                        w.partner = m
                        m.partner = w
