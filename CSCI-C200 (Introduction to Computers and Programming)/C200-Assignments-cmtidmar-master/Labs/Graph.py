class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i]=[]
    def add_edge(self, pair):
        start, end = pair
        self.edges[start].append(end)
    def children(self, node):
        return self.edges[node]
    def nodes(self):
        return str(self.nodes)
    def __str__(self):
        return str(self.edges)
        