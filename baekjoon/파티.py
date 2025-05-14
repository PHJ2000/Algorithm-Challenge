"""
사이트: 백준
문제 이름: [파티](https://www.acmicpc.net/problem/1238)

풀이 접근 방법:
- 다익스트라(Dijkstra) 알고리즘을 사용하여 최단 경로 계산
- 정방향 그래프: X에서 각 마을로 가는 최단 거리 계산
- 역방향 그래프: 각 마을에서 X로 오는 최단 거리 계산
- 각 마을의 왕복 시간을 계산 후, 최대 왕복 시간 출력

느낀점:
- 역방향 그래프를 이용한 역방향 탐색이 인상적이었음
- 다익스트라를 2번 활용하여 효율적으로 문제를 해결할 수 있었음
- 힙 자료구조와 시간 복잡도의 중요성을 다시금 실감함
"""
import sys
import heapq

def dijkstra(start, graph, n):
    INF = int(1e9)
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, now = heapq.heappop(heap)
        if dist[now] < cost:
            continue
        for next_node, weight in graph[now]:
            next_cost = cost + weight
            if dist[next_node] > next_cost:
                dist[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))
    return dist

def main():
    input = sys.stdin.readline
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        reverse_graph[v].append((u, w))

    to_X = dijkstra(X, reverse_graph, N)
    from_X = dijkstra(X, graph, N)

    max_time = 0
    for i in range(1, N + 1):
        total_time = to_X[i] + from_X[i]
        if total_time > max_time:
            max_time = total_time

    print(max_time)

if __name__ == "__main__":
    main()
