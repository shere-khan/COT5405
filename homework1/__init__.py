from homework1 import stable_marriage as sm

if __name__ == '__main__':
    SIZE = 6
    mens_stack = ['d', 'g', 'a', 'm', 'j', 't']
    womens_stack = ['ka', 's', 't', 'ky', 'f', 'j']

    men = []
    women = []
    sm.Game.create_players_hard(men, women)
    sm.Game.set_preferences_hard(men, women)

    sm.Game.gale_shapley(men)
    sm.Game.print_info(men, women)
