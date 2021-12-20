from bestgraph import Graph

def main():
    print("Testing code below")
    print("="*30)

    givenNodes = [1, 2, 3, 4]

    givenEdges = [(1, 2), (1, 3), (3, 4)]

    g = Graph(givenNodes)

    print("Testing adding original edges")
    print("=" * 10)
    for e in givenEdges:
        result = g.add_edge(e)
        if result == -1:
            print("Adding edges " + str(e) + " should have returned 1. Returned -1")

    print("=" * 10 + "\n")

    print("Testing Add Node")

    addNodes = [1, 5, 6, 7]
    results = [-1, 1, 1, 1]

    print("=" * 10)
    for i in range(len(addNodes)):
        toAdd = addNodes[i]
        correct = results[i]
        result = g.add_node(toAdd)
        if result != correct:
            print("Adding nodes " + str(toAdd) + " should have returned " + str(-1 * result) + ". Returned " + str(result))
    print("=" * 10 + "\n")


    print("Testing Add Edge")

    addEdges = [(1, 2), (2, 5), (3, 2), (2, 7), (7, 2)]
    addResults = [-1, 1, 1, 1, 1]

    print("=" * 10)
    for i in range(len(addEdges)):
        toAdd = addEdges[i]
        correct = addResults[i]
        result = g.add_edge(toAdd)
        if result != correct:
            print("Adding edges " + str(toAdd) + " should have returned " + str(-1 * result) + ". Returned " + str(result))
    print("=" * 10 + "\n")

    # FIXME: This does not test if you adjacency Matrix is created correctly. If you want to ensure it works, you need to write your own tests (required)
    # m1 = [(1, 2), (1, 3), (3, 4)] #Also messed this one up
    # print(adjacencyMatrix(m1))

    # FIXME: This does not test if you delete nodes and edges correctly. If you want to ensure it works, you need to write your own tests (required)
   
    print("Testing deleting nodes and edges") #I definitely hink i screwed up the testing for this 
    # delNodes = [1, 5, 6, 7]
    # for i in range(len(delNodes)):
    #     toDel = delNodes[i]
    #     correct = delNodes[i]
    #     result = g.del_node(toDel)
    #     if result != correct:
    #         print("incorrect")

    print("Testing deleting nodes and edges") #I definitely think i screwed up the testing for this 
    # delEdges = [(1, 2), (2, 5), (3, 2), (2, 7), (7, 2)]
    # for i in range(len(delEdges)):
    #     toDel = delEdges[i]
    #     correct = delEdges[i]
    #     result = g.del_edge(toDel)
    #     if result != correct:
    #         print("incorrect")
        

if __name__ == "__main__":
        main()
