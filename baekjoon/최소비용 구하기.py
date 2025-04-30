"""
사이트: 백준  
문제 이름: [최소비용 구하기](https://www.acmicpc.net/problem/1916)

풀이 접근 방법:
- 다익스트라 알고리즘을 사용해 한 정점에서 다른 정점까지의 최소 비용 계산
- 우선순위 큐(heapq)를 사용해 방문할 정점을 효율적으로 선택
- 거리 배열(distance)을 사용해 각 정점까지의 최소 비용을 저장
- 이미 최적 경로가 확정된 노드는 다시 방문하지 않도록 최적화

느낀점:
- 다익스트라 알고리즘의 흐름을 직접 구현하면서 자료구조의 중요성을 체감함
- heapq를 사용한 우선순위 큐의 작동 방식이 익숙해졌고,
  단일 시작점 최단경로 문제에서의 전형적인 패턴을 익힐 수 있었음
"""
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, cost = map(int, input().strip().split())
    graph[u].append((v, cost))

start, end = map(int, input().strip().split())

distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

dijkstra(start)
print(distance[end])
