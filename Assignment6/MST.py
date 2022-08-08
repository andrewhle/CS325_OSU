def Prims(G):
    # Prim's Algorithm in Python


    INF = 9999999
    # number of vertices in graph
    V = len(G)
    # create a 2d array of size 5x5
    # for adjacency matrix to represent graph

    # create a array to track selected vertex
    # selected will become true otherwise false
    result = []
    selected = [0] * len(G)
    # set number of edge to 0
    no_edge = 0
    # the number of egde in minimum spanning tree will be
    # always less than(V - 1), where V is number of vertices in
    # graph
    # choose 0th vertex and make it true
    selected[0] = True
    # print for edge and weight
    print("Edge : Weight\n")
    while (no_edge < V - 1):
        # For every vertex in the set S, find the all adjacent vertices
        # , calculate the distance from the vertex selected at step 1.
        # if the vertex is already in the set S, discard it otherwise
        # choose another vertex nearest to selected vertex  at step 1.
        minimum = INF
        x = 0
        y = 0
        for i in range(V):

            if selected[i]:
                for j in range(V):
                    
                    if ((not selected[j]) and G[i][j]):
                        # not in selected and there is an edge
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
        result.append(tuple((x, y, minimum)))
        selected[y] = True
        no_edge += 1

    print(result)
    return result

G = [[0, 8, 5, 0, 0, 0, 0], 
  [8, 0, 10, 2, 18, 0, 0], 
  [5, 10, 0, 3, 0, 16, 0], 
  [0, 2, 3, 0, 12, 30, 14], 
  [0, 18, 0, 12, 0, 0, 4], 
  [0, 0, 16, 30, 0, 0, 26], 
  [0, 0, 0, 14, 4, 26, 0]]


Prims(G)