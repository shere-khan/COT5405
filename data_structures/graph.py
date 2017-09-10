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

    def add_node(self, node):
        # If only node parameter, add the node to the dict
        # with a None value
        self.__adj_dict[node] = list()

    def add_connection(self, node, neighbor):
        self.__adj_dict[node].append(neighbor)
        self.__adj_dict[neighbor].append(node)

    def size(self):
        n = 0
        for node, adj_list in self.__adj_dict.items():
            if adj_list:
                n += len(adj_list)

        n += len(self.__adj_dict)

        return n

    def get_random_node(self):
        node_key = random.sample(list(self.get_adj_dict()), 1)[0]
        node_list = self.get_adj_dict()[node_key]
        node = random.sample(node_list, 1)[0]

        return node


class GraphData:
    # TODO implement interval_size_lim range
    @staticmethod
    def populate_graph(graph, interval_size_lim, total_size):
        # Add a node by default
        first_node = Node()
        node_value = 0
        first_node.set_value(node_value)
        node_value += 1

        # If the graph has not yet been populated, add another node
        # and connect it to the first node
        graph.add_node(first_node)
        if graph.size() is 1:
            second_node = Node()
            second_node.set_value(node_value)
            node_value += 1

            graph.add_node(second_node)
            graph.add_connection(first_node, second_node)

        # Start populating the rest of the graph
        while graph.size() < total_size:
            limit = 0
            new_node = Node()
            new_node.set_value(node_value)
            node_value += 1
            graph.add_node(new_node)
            while limit < interval_size_lim:
                # Get random key (node) from adjacency dict
                neighb_key = random.sample(list(graph.get_adj_dict()), 1)[0]
                # Get the adjacency list corresponding to the key
                neighb_list = graph.get_adj_dict()[neighb_key]
                if neighb_list is not None and len(neighb_list) > 0:
                    neighb = random.sample(neighb_list, 1)[0]
                    # Get the adjacency list for the new node
                    new_node_neighbor_list = graph.get_adj_dict()[new_node]
                    # If neighb is not the node we just added make it a connection of new_node
                    if neighb is not new_node and neighb not in new_node_neighbor_list:
                            graph.add_connection(new_node, neighb)
                            limit += 1

                            if limit is interval_size_lim:
                                break

    @staticmethod
    def breadth_first_traversal(graph, node, f):
        # f(node)
        print(node.get_value())
        node.discovered = True
        to_visit_queue = [node]
        while to_visit_queue:
            u = to_visit_queue.pop(0)
            neighbors = graph.get_adj_dict()[u]
            for v in neighbors:
                if v.discovered is False:
                    # f(node)
                    print(v.get_value())
                    v.discovered = True
                    to_visit_queue.append(v)
