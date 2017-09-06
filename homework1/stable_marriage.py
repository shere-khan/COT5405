class Person:
    def __init__(self):
        self.preference_list = []


class Man(Person):
    def __init__(self):
        Person.__init__(self)


class Woman(Person):
    def __init__(self):
        Person.__init__(self)
