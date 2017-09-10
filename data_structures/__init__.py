from data_structures import graph as g

if __name__ == '__main__':
    graph = g.UndirectedGraph()
    g.GraphData.populate_graph(graph, 2, 20)
    g.GraphData.breadth_first_traversal(graph, graph.get_random_node(), lambda x: print(x.get_value()))
