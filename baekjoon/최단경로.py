"""
사이트: 백준  
문제 이름: [최단경로](https://www.acmicpc.net/problem/1753)

풀이 접근 방법:
- 다익스트라 알고리즘 사용
- 시작 정점으로부터 우선순위 큐(heapq)를 통해 최단 거리 갱신
- 거리 배열(distance[])을 통해 각 정점까지의 최소 비용 저장
- 간선 정보는 인접 리스트로 구성하여 효율적인 탐색 수행

느낀점:
- 다익스트라 기본 구현에 익숙해질 수 있는 대표 문제
- 간선 수가 많아도 우선순위 큐를 사용하면 충분히 빠르게 해결 가능
- 방문 조건 체크(`if distance[now] < dist`)가 불필요한 연산을 방지하는 핵심
"""
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

dijkstra(K)

for i in range(1, V + 1):
    print("INF" if distance[i] == INF else distance[i])
