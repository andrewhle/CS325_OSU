
def helper(G, s, visited, src, cost):
    while s not in visited:
        edges = G[s]

        min_weight = -1
        min_node = -1
        visited.append(s)

        for (i, j) in enumerate(edges):
            
            if(min_weight == -1) and (j != 0) and (i not in visited):
                min_weight = j
                min_node = i
            elif(min_weight != -1) and (j != 0) and (j < min_weight) and (i not in visited):
                min_weight = j
                min_node = i

        if min_node != -1:
            s = min_node
        if min_weight != -1:
            cost = cost + min_weight
    
    cost = cost + G[s][src]
    visited.append(visited[0])
    print("Cost =", cost)
    print(visited)
    return visited

def solve_tsp(G):
    s = 0
    visited = []
    src = s
    cost = 0

    return helper(G, s, visited, src, cost)

G = [ 
    [0, 2, 3, 20, 1], 
    [2, 0, 15, 2, 20], 
    [3, 15, 0, 20, 13], 
    [20, 2, 20, 0, 9], 
    [1, 20, 13, 9, 0], 
] 

solve_tsp(G)


