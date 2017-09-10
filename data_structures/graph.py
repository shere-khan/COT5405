import random


class Edge:
    def __init__(self):
        self.__node_id = ""
        self.__discovered = False
        self.__weight = 0

    def set_node_id(self, value):
        self.__node_id = value

    def get_node_id(self):
        return self.__node_id

    def set_discovered(self, discovered):
        self.__discovered = discovered

    def get_discovered(self):
        return self.__discovered

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight


class UndirectedGraph:
    def __init__(self):
        self.__adj_dict = dict()
        self.__node_list = list()
        self.__edge_list = list()

    def get_adj_dict(self):
        return self.__adj_dict

    def set_adj_dict(self, adj_dict):
        self.__adj_dict = adj_dict

    def add_edge(self, edge):
        # If only node parameter, add the edge to the dict
        # with a None value
        self.__adj_dict[edge] = list()

    def add_connection(self, edge, neighbor):
        self.__adj_dict[edge].append(neighbor)
        self.__adj_dict[neighbor].append(edge)

    def size(self):
        n = 0
        for edge, adj_list in self.__adj_dict.items():
            if adj_list:
                n += len(adj_list)

        n += len(self.__adj_dict)

        return n

    def get_random_edge(self):
        node_key = random.sample(list(self.get_adj_dict()), 1)[0]
        node_list = self.get_adj_dict()[node_key]
        node = random.sample(node_list, 1)[0]

        return node


class GraphData:
    # TODO implement interval_size_lim range
    @staticmethod
    def populate_graph(graph, interval_size_lim, total_size):
        # Add a edge by default
        first_edge = Edge()
        node_id_value = 0
        first_edge.set_node_id(node_id_value)
        node_id_value += 1

        # If the graph has not yet been populated, add another edge
        # and connect it to the first edge
        graph.add_edge(first_edge)
        if graph.size() is 1:
            second_edge = Edge()
            second_edge.set_node_id(node_id_value)
            node_id_value += 1

            graph.add_edge(second_edge)
            graph.add_connection(first_edge, second_edge)

        # Start populating the rest of the graph
        while graph.size() < total_size:
            limit = 0
            new_edge = Edge()
            new_edge.set_node_id(node_id_value)
            node_id_value += 1
            graph.add_edge(new_edge)
            while limit < interval_size_lim:
                # Get random key (edge) from adjacency dict
                neighb_key = random.sample(list(graph.get_adj_dict()), 1)[0]
                # Get the adjacency list corresponding to the key
                neighb_list = graph.get_adj_dict()[neighb_key]
                if neighb_list is not None and len(neighb_list) > 0:
                    neighb = random.sample(neighb_list, 1)[0]
                    # Get the adjacency list for the new edge
                    new_neighbor_list = graph.get_adj_dict()[new_edge]
                    # If neighb is not the edge we just added make it a connection of new_edge
                    if neighb is not new_edge and neighb not in new_neighbor_list:
                        graph.add_connection(new_edge, neighb)
                        limit += 1

                        if limit is interval_size_lim:
                            break

    @staticmethod
    def breadth_first_traversal(graph, edge, f):
        f(edge)
        edge.set_discovered(True)
        to_visit_queue = [edge]
        while to_visit_queue:
            u = to_visit_queue.pop(0)
            neighbors = graph.get_adj_dict()[u]
            for v in neighbors:
                if v.get_discovered() is False:
                    f(v)
                    v.set_discovered(True)
                    to_visit_queue.append(v)
