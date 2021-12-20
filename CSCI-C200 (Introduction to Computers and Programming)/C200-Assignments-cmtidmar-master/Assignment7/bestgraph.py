class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []

    def add_edge(self, pair):
        start, end = pair
        
        # If either node does not exist in the graph, return -1
        if start not in self.nodes or end not in self.nodes:
            return -1
        
        # If the edge connection already exists, return -1
        connections = self.edges[start]
        if end in connections:
            return -1
        
        # If successfully able to add the pair of nodes to the graph, return 1
        self.edges[start].append(end)
        return 1

    def children(self, node):
        return self.edges[node]

    def nodes(self):
        return str(self.nodes)
        if self.nodes == self.nodes:
            return -1
        else:
            return 1
        
    def add_node(self, node):
        #Add a node, return -1 if node already exists.
        if node not in self.nodes:
            self.edges[node] = []
            self.nodes.append(node)
            return 1
        else:
            return -1
      
    
    
    def del_node(self, node):
        
        if node not in self.nodes:
            return -1
        if node in self.nodes:
            self.nodes.remove(node)
            self.edges.pop(node)
            return 1
        

    def del_edge(self, pair):
        start, end = pair
        if end not in self.edges[start]:
            return -1
        else:
            connections = self.edges[start]
            connections.remove(end)
            return 1

    def adjacencyMatrix(self):
        maxtrix = []
        for row in matrix:
            temp = []
            for column in row:
                if column % 2 == 0:
                    temp += [column *2]
                else:
                    temp += [column]
            matrix += [ temp ]
        return matrix





   

    def __str__(self):
        return str(self.edges)