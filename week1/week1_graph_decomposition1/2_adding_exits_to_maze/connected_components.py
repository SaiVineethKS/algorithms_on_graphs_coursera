#Uses python3

import sys

def dfs(node, adj, visited):
    if len(adj[node]) == 0 or node in visited:
        return
    visited.append(node)
    for next_node in adj[node]:
        dfs(next_node, adj, visited)

def number_of_components(adj):
    result = 0
    #write your code here
    visited = []
    for node in range(len(adj)):
        if node not in visited:
            dfs(node, adj, visited)
            result += 1
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
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
