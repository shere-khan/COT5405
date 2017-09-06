from homework1 import stable_marriage as sm
from copy import deepcopy

if __name__ == '__main__':
    SIZE = 5
    womens_stack = ['suzy', 'katrina', 'felicia', 'jenae', 'kyana']
    womens_names = deepcopy(womens_stack)
    mens_stack = ['germaine', 'michael', 'andre', 'justin', 'tim']
    mens_names = deepcopy(mens_stack)

    women = []
    men = []
    sm.Game.create_players(men, women, mens_stack, womens_stack)
    sm.Game.set_preferences(men, women, mens_names, womens_names)
    # sm.Game.set_preferences(men, women)

    # for m in men:
    #     print(m.preferences_map)

    sm.Game.gale_shapley(men)
