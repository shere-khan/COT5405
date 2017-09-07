import unittest

from homework1 import stable_marriage as sm


class TestGame(unittest.TestCase):
    def setUp(self):
        SIZE = 5
        womens_stack = ['suzy', 'katrina', 'felicia', 'jenae', 'kyana']
        mens_stack = ['germaine', 'michael', 'andre', 'justin', 'tim']

        women = []
        self.men = []
        sm.Game.create_players(men, women, mens_stack, womens_stack)
        sm.Game.set_preferences(men, women, SIZE)

    def test_gale_shapley_pairs_stable(self):
        sm.Game.gale_shapley(self.men)
        for m in self.men:
            if m.name != w.partner.name:
                w_preferred_partner_index = self.men.index(w.partner)
                w_preferred_partner = self.men[w.partner_index]
                w_preferred_partner_preference = w_preferred_partner.preference_list[0]
                if w_preferred_partner_preference.name is w.name:
                    pass

            for w in m.preference_list:
                if (m.partner)
