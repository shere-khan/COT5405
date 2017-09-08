class UndirectedGraph:
    def __init__(self):
        self.__adj_dict = dict()

    def get_adj_dict(self):
        return self.__adj_dict

    def set_adj_dict(self, adj_dict):
        self.__adj_dict = adj_dict


class Node:
    def __init__(self):
        self.__value = ""

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value
