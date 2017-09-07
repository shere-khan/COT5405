from copy import deepcopy

from homework1 import stable_marriage as sm

if __name__ == '__main__':
    SIZE = 6
    mens_stack = ['d', 'g', 'a', 'm', 'j', 't']
    womens_stack = ['ka', 's', 't', 'ky', 'f', 'j']
    # womens_stack = ['suzy', 'katrina', 'felicia', 'jenae', 'kyana']
    # mens_stack = ['germaine', 'michael', 'andre', 'justin', 'tim']

    men = []
    women = []
    # sm.Game.create_players(men, women, mens_stack, womens_stack)
    # sm.Game.set_preferences(men, women, SIZE)
    sm.Game.create_players_hard(men, women)
    sm.Game.set_preferences_hard(men, women)
    # sm.Game.print_info(men, women)
    sm.Game.gale_shapley(men)
    sm.Game.print_info(men, women)
