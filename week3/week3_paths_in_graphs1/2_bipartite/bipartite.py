#Uses python3

import sys
import queue

def is_bipartite(adj, v, visited, color) -> bool:
    q = []
    q.append(v)
    color[v] = 0
    while len(q) > 0:
        node = q.pop(0)
        for next_n in adj[node]:
            if color[next_n] > -1 and color[next_n] == color[node]:
                # Not bipartite
                return False
            
            # Change 0 to 1 or 1 to 0 color, vice versa
            color[next_n] = (color[node] + 1) % 2

            if next_n not in visited:
                visited.add(next_n)
                q.append(next_n)
    
    return True

def bipartite(adj):
    """
    Loop through all nodes in the graph and maintain a visited set

    For every node that is not visited, give it a color and perform a BFS
    During the BFS check if there is a node in the next level with the same color as currently processed node
    If yes, then this graph cannot be bipartite,
    i.e You cannot seperate out the set of vertices in the graph such that all edges are connected to 
    one vertice from each set

    If you can color the entire graph (while maintaing a global visited set)
    without adjacent nodes in the graph needing the same color, then your graph is bipartite

    Note: this method can also performed with prev[node] concept, however you still need to process all none visited nodes
    in a single BFS graph.

    Remember input can be a directed graph too, visit all the nodes and color them
    """
    visited = set([])
    color = [-1] * len(adj)
    for v in range(len(adj)):
        if v in visited:
            continue
        visited.add(v)
        if not(is_bipartite(adj, v, visited, color)):
            return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
