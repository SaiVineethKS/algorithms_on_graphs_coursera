#Uses python3

import sys

def findcycle(adj, node:int, visited, stack) -> bool:
    visited[node]  = True
    stack[node] = True

    for child in adj[node]:
        # If child node has cycles then return True (we found cycle)
        if child not in visited:
            if findcycle(adj, child, visited, stack):
                return True
        # If child node is visited in a different recursion, but probably not in our current recursion stack
        # Therefore check if the child is in our current recrusion stack, only then we can determine it is a cycle
        elif child in stack:
            return True
    
    # Remove current node from our current recursion stack, so that it can be used for next one
    stack[node] = False 
    return False

def acyclic(adj):
    visited = [False] * len(adj)
    stack = [False] * len(adj)
    for node in range(len(adj)):
        if not visited[node]:
            if findcycle(adj, node, visited, stack):
                return False
    return True

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    n, m = 5, 7
    data = [1,2,2,3,1,3,3,4,1,4,5,2,3,5]
    # n, m = 4, 4
    # data = [1,2,4,1,2,3,3,1]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(adj)
    print(acyclic(adj))
