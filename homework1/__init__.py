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
    sm.Game.set_preferences(men, women, SIZE)
    sm.Game.gale_shapley(men)

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
