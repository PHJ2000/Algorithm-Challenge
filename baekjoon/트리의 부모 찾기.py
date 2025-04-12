"""
사이트: 백준
문제 이름: [트리의 부모 찾기](https://www.acmicpc.net/problem/11725)

풀이 접근 방법:
- 1부터 시작해서, bfs로 값을 찾고, 찾기 직전에 있던 값을 출력하면 된다. bfs는 N, N = N^2
- 100000^2=10000000000 안된다. 한 번의 탑색으로 다 찾자. 일단 루트가 정해져 있으니, 큐에 들어가져
- 있으면, 무조건 부모를 알 수 있다. 즉 bfs를 한 번만 수행하면 된다.
- 트리는 리스트로 만들자. 이중 리스트를 어떻게 만들지?

느낀점:
- 방문 체크를 실수 하였다. vu[i]로 체크 해야하는데, vi[p]로 해서 틀린 결과가 나왔었다. 방문체크를
- 주의해야겠다.
"""
from collections import deque

N = int(input())
l = [[] for _ in range(N)]
ch = [0] * N
vi = [False] * N
d = deque()

for _ in range(N - 1):
    s, e = map(int, input().split())
    l[s - 1].append(e - 1)
    l[e - 1].append(s - 1)

d.append(0)
vi[0] = True

while d:
    p = d.popleft()
    for i in l[p]:
        if not vi[i]:
            vi[i] = True
            ch[i] = p
            d.append(i)

for i in range(1, N):
    print(ch[i] + 1)
