#Uses python3

import sys

sys.setrecursionlimit(200000)

def reverse_graph(adj):
    r_adj = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for e in adj[i]:
            r_adj[e].append(i)
    return r_adj

def dfs(adj, used, order, x):
    """
    The key idea here is to pick a source node
    keep DFSing till it reaches a sink node
    
    Due to the lack of adjacent nodes, sink node will 
    return its function call. Followed by a series of 
    'returns' from all functional calls in the stack
    until the initial source node's call.

    Here, append the initial source node to graph
    """
    if used[x] == 1:
        # If x is already used in the toposort
        return
    
    # Keep tracking if the current 
    # variable is already during the DFS process
    used[x] = 1
    
    for e in adj[x]:
        # Keep DFSing till you find a sink
        dfs(adj, used, order, e)
    
    # Once a sink is found add the initial node
    # the recursion call stack
    order.append(x)

def explore(v, adj, path, visited):
    if v in path or v in visited:
        return

    visited.append(v)
    path.append(v)

    for e in adj[v]:
        explore(e, adj, path, visited)

def number_of_strongly_connected_components(adj):
    result = 0
    r_adj = reverse_graph(adj)
    used = [0] * len(r_adj)
    post_order = []
    visited = []
    path = []
    # Get postorder of reversed graph
    for v in range(len(r_adj)):
        dfs(r_adj, used, post_order, v)
    
    # Reverse the post order
    post_order.reverse()

    # For every vertex in the post order
    # Explore all possible vertices reachable from the vertex
    # Create a path out of it and record that as an SCC
    for v in post_order:
        if v not in visited:
            explore(v, adj, path, visited)
            result += 1
            path = []

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
