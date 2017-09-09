import random


class Node:
    def __init__(self):
        self.__value = ""
        self.discovered = False

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value


class UndirectedGraph:
    def __init__(self):
        self.__adj_dict = dict()

    def get_adj_dict(self):
        return self.__adj_dict

    def set_adj_dict(self, adj_dict):
        self.__adj_dict = adj_dict

    def add_node(self, node, **kwargs):
        self.__adj_dict[node] = None
        for name, value in kwargs.items():
            if name is 'neighbors':
                neighbors = name
                self.__adj_dict[node] = neighbors
                for n in neighbors:
                    self.__adj_dict[n] = node

    def add_connection(self, node, neighbor):
        self.__adj_dict[node].append(neighbor)

    def size(self):
        n = 0
        for node, adj_list in self.__adj_dict.items():
            if adj_list:
                n += len(adj_list)

        n += len(self.__adj_dict)
        return n

    @staticmethod
    def breadth_first_traversal(node):
        node.discovered = True
        to_visit_queue = list(node)
        while to_visit_queue:
            u = to_visit_queue.pop(0)
            neighbors = u.__adj_dict[node]
            for v in neighbors:
                if v.discovered is False:
                    v.discovered = True
                    to_visit_queue.append(v)


class GraphData:
    # TODO implement interval_size_lim
    @staticmethod
    def populate_graph(graph, interval_size_lim, total_size):
        # Add a node by default
        first_node = Node()

        # If the graph has not yet been populated, add another node
        # and connect it to the first node
        graph.add_node(first_node)
        if graph.size() is 1:
            graph.add_node(Node(), first_node)

        # Start populating the rest of the graph
        while graph.size() < total_size:
            limit = 0
            new_node = Node()
            graph.add_node(Node(), new_node)
            while limit < interval_size_lim:
                neighb_key = random.sample(list(graph.get_adj_dict()), 1)
                neighb_list = graph.get_adj_dict()[neighb_key]
                neighb = random.sample(neighb_list, 1)

                # If neighb is not the node we just added
                # make it a connection of new_node
                if neighb is not new_node:
                    graph.add_connection(new_node, neighb)
                    limit += 1

                    if limit is interval_size_lim:
                        break
            #
