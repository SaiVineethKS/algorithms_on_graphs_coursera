#Uses python3

import sys
import queue
import math

def distance(adj, start, end):
    #write your code here
    queue,visited = [], []
    queue.append(start)
    visited.append(start)
    distance = [math.inf] * len(adj)
    distance[start] = 0
    while len(queue) > 0:
        node = queue.pop(0)
        if node == end:
            return distance[node]
        visited.append(node)
        for next_node in [n for n in adj[node] if n not in visited]:
            distance[next_node] = distance[node] + 1
            queue.append(next_node)
    return -1

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    data = [4,4,1,2,4,1,2,3,3,1,2,4]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
