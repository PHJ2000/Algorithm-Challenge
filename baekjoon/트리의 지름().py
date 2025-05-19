import sys
from collections import deque

def bfs(start, adj):
    n = len(adj)
    dist = [-1] * n
    q = deque([start])
    dist[start] = 0
    while q:
        cur = q.popleft()
        for nxt, w in adj[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + w
                q.append(nxt)
    far_node = dist.index(max(dist))
    far_dist = dist[far_node]
    return far_node, far_dist

input = sys.stdin.readline
V = int(input())
adj = [[] for _ in range(V + 1)]
for _ in range(V):
    line = list(map(int, input().split()))
    u = line[0]
    i = 1
    while line[i] != -1:
        v, w = line[i], line[i + 1]
        adj[u].append((v, w))
        adj[v].append((u, w))
        i += 2
A, _ = bfs(1, adj)
_, diameter = bfs(A, adj)
print(diameter)


