#Uses python3

import sys
import queue

def distance(adj, s, t):
    """
    Do not initialize infinity for distance node, the concept fails, instead carry the distance like a tuple
    Note: There is path from 's' to 't' if 's' == 't', only if the graph has a self-referential link
    Else the distance is -1 i.e infinity
    """
    q, visited = [], set([])
    q.append((1,s))
    while len(q) > 0:
        distance, node = q.pop(0)
        visited.add(node)
        if t in adj[node]:
            return distance
        for e in adj[node]:
            if e not in visited:
                q.append((distance+1, e))
    return -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
