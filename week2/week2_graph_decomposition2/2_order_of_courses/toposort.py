#Uses python3

import sys

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

def toposort(adj):
    used = [0] * len(adj)
    postvisit_order = []
    
    for v in range(len(adj)):
        dfs(adj, used, postvisit_order, v)

    # Actual topological sort is the reverse
    # of post-visit order
    return reversed(postvisit_order)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

