import unittest

from homework1 import stable_marriage as sm


class TestGame(unittest.TestCase):
    def setUp(self):
        SIZE = 5
        womens_stack = ['suzy', 'katrina', 'felicia', 'jenae', 'kyana']
        mens_stack = ['germaine', 'michael', 'andre', 'justin', 'tim']

        women = []
        self.men = []
        sm.Game.create_players(self.men, women, mens_stack, womens_stack)
        sm.Game.set_preferences(self.men, women, SIZE)

    def test_gale_shapley_pairs_stable(self):
        sm.Game.gale_shapley(self.men)
        for m in self.men:
            w = m.partner
            # If the current man is not his partner's preferred partner,
            # then check if her preferred partner would also prefer her
            w_preferred_partner = w.preference_list_copy[0]
            if m is not w_preferred_partner:
                w_preferred_partner_preference = w_preferred_partner.preference_list[0]
                assert w_preferred_partner_preference.name is not w.name

            # If the mans current partner is not his preferred partner,
            # then check if man would rather be with someone else
            preferred_partner = m.preference_list_copy[0]
            if m.partner is not preferred_partner:
                pref = preferred_partner.preference_list_copy[0]
                assert pref.name is not m.name
