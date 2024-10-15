class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for node1, node2 in edges:
            self.data[node1].append(node2)
            self.data[node2].append(node1)
    
    def __repr__(self):
        # Adjacency List
        return "\n".join(["{}:{}".format(node, neighbor) for node, neighbor in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()