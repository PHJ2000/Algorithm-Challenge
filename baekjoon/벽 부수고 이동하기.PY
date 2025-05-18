"""
사이트: 백준
문제 이름: [벽 부수고 이동하기](https://www.acmicpc.net/problem/2206)

풀이 접근 방법:
- BFS와 3차원 visited 배열을 활용해 최단 거리 탐색
- 벽을 한 번까지 부술 수 있으므로, (x, y, 벽 부숨 여부)로 상태를 관리
- 큐에 벽을 부순 상태/안 부순 상태를 따로 넣으며 탐색

느낀점:
- 벽 부숨 여부에 따라 visited 상태를 나누는 아이디어가 인상적이었음
- BFS를 여러 상태로 확장하는 방법을 배움
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().strip())) for _ in range(n)]
v = [[[0]*2 for _ in range(m)] for _ in range(n)]
q = deque([(0, 0, 0)])
v[0][0][0] = 1
d = [(1,0),(-1,0),(0,1),(0,-1)]

while q:
    x, y, w = q.popleft()
    if x == n-1 and y == m-1:
        print(v[x][y][w])
        exit()
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m:
            if g[nx][ny]==0 and v[nx][ny][w]==0:
                v[nx][ny][w] = v[x][y][w]+1
                q.append((nx, ny, w))
            elif g[nx][ny]==1 and w==0 and v[nx][ny][1]==0:
                v[nx][ny][1] = v[x][y][w]+1
                q.append((nx, ny, 1))
print(-1)
