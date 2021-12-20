
from Stack import Stack
from Queue import Queue
from Graph import Graph

#----------------------W/Out Lecturer---------------------------
"""
def DFS-A(G, s): # Pretty sure incorrect
    for all v in V[G]:
        visited[v] == False
    end for S == EmptyStack
    Push(S, s)

    while not Empty(S):
        u == Pop(S)
        if not visited[u]:
            visted[u] == True
            for all in Adj[u]:
                if not visited[w]:
                    Push(S, w)
                end if
            end for 
        end if
    end while



    def BFS(G):
        for all v in V:
            if v == 0:
                bfs(v)
        return bfs(v) # Not quite sure about this

        while queue not empty:
            for w in adj[V]:
                if w == 0:
                    count += 1
                    Queue.append(w) # or Queue.insert(w)
                    w == [1] #Bc append appends the value to the end, you need to move it to the first position
            Queue.remove[0] # Remove the front vertex from queue, so w will be first
"""
#------------------------------------------------------------

#----------------------W/ Lecturer---------------------------
def dfs(g, s):
    visited = []
    st = Stack()
    st.push(s) #Assuming s is in g
    while not st.isEmpty():
        cn = st.pop()
        if cn not in visited:
            visited.append(cn)
            for c in g.children(cn):
                if c not in visited:
                    st.push(c)
    return visited
    

def bfs(g, s):
    visited = []
    st = Queue()
    st.enqueue(s) #Assuming s is in g
    while not st.isEmpty():
        cn = st.dequeue()
        if cn not in visited:
            visited.append(cn)
            for c in g.children(cn):
                if c not in visited:
                    st.enqueue(c)
    return visited


if __name__ == "__main__":
    ourGraph = Graph(["a", "b", "c", "d", "e", "f"])
    edges = [("a", "c"), ("c", "b"), ("a", "d"), ("d", "e"), ("e", "f"), ("c", "e"), ("b", "f")]
    for e in edges:
        ourGraph.add_edge(e)
        ourGraph.add_edge((e[1], e[0]))
    print(dfs(ourGraph, "a"))
    print(bfs(ourGraph, "a"))

