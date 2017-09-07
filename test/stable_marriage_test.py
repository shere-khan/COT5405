import unittest

from homework1 import stable_marriage as sm


class TestGame(unittest.TestCase):
    def setUp(self):
        SIZE = 6
        mens_stack = ['d', 'g', 'a', 'm', 'j', 't']
        womens_stack = ['ka', 's', 't', 'ky', 'f', 'j']
        # womens_stack = ['suzy', 'katrina', 'felicia', 'jenae', 'kyana']
        # mens_stack = ['germaine', 'michael', 'andre', 'justin', 'tim']

        self.men = []
        self.women = []
        # sm.Game.create_players(men, women, mens_stack, womens_stack)
        # sm.Game.set_preferences(men, women, SIZE)
        sm.Game.create_players_hard(self.men, self.women, mens_stack, womens_stack)
        sm.Game.set_preferences_hard(self.men, self.women)
        # sm.Game.print_info(men, women)

        # SIZE = 6
        # womens_stack = ['suzy', 'katrina', 'felicia', 'jenae', 'kyana', 'tina']
        # mens_stack = ['germaine', 'michael', 'andre', 'justin', 'tim', 'drake']

        # self.women = []
        # self.men = []
        # sm.Game.create_players(self.men, self.women, mens_stack, womens_stack)
        # sm.Game.set_preferences(self.men, self.women, SIZE)

    def test_gale_shapley_pairs_stable(self):
        sm.Game.gale_shapley(self.men)

        sm.Game.print_info(self.men, self.women)

        # run test
        for m in self.men:
            w = m.partner
            # If the current man is not his partner's preferred partner,
            # then check if her preferred partner would also prefer her
            w_preferred_partner = w.preference_list_copy[0]
            if m is not w_preferred_partner:
                w_preferred_partner_preference = w_preferred_partner.preference_list[0]
                try:
                    assert w_preferred_partner_preference.name is not w.name
                except AssertionError:
                    print("m.partner: ", m.partner)
                    print("w.preferred_partner: ", w_preferred_partner.name)
                    print("w.preferred_partner_preference: ", w_preferred_partner_preference.name)
                    raise AssertionError

            # If the mans current partner is not his preferred partner,
            # then check if man would rather be with someone else
            preferred_partner = m.preference_list_copy[0]
            if m.partner is not preferred_partner:
                preferred_partner_preference = preferred_partner.preference_list_copy[0]
                try:
                    assert preferred_partner_preference.name is not m.name
                except AssertionError:
                    print("m.partner: ", m.partner)
                    print("m.preferred_partner: ", preferred_partner.name)
                    print("m.preferred_partner: ", preferred_partner_preference.name)
                    raise AssertionError
