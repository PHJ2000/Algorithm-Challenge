"""
사이트: 백준
문제 이름: [웜홀](https://www.acmicpc.net/problem/1865)

풀이 접근 방법:
- 벨만-포드 알고리즘을 이용하여 음의 사이클(음수 사이클)이 존재하는지 판단
- 모든 정점에서 시작하지 않고, 거리 배열을 0으로 초기화하여 한 번만 벨만-포드 수행
- N번째 라운드에서 값이 갱신되면 음의 사이클 존재

느낀점:
- 음의 사이클 판별 문제를 풀며 벨만-포드 알고리즘의 응용을 체감함
- 모든 정점에서 돌리는 것보다 효율적인 구현 방법을 익힘
"""
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        S, E, T_ = map(int, input().split())
        edges.append((S, E, T_))
        edges.append((E, S, T_))
    for _ in range(W):
        S, E, T_ = map(int, input().split())
        edges.append((S, E, -T_))
    
    dist = [0] * (N + 1)
    has_negative_cycle = False

    for i in range(N):
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if i == N - 1:
                    has_negative_cycle = True

    print("YES" if has_negative_cycle else "NO")
