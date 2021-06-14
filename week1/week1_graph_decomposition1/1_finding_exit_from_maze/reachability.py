#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    queue,visited = [], []
    queue.extend(adj[x])
    visited.append(x)
    has_path = 0
    while len(queue) > 0:
        node = queue.pop(0)
        if node == y:
            has_path = 1
            break
        visited.append(node)
        next_nodes = [n for n in adj[node] if n not in visited]
        queue.extend(next_nodes)
    return has_path

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
