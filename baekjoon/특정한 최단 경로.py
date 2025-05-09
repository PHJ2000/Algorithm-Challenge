"""
사이트: 백준  
문제 이름: [특정한 최단 경로](https://www.acmicpc.net/problem/1504)

풀이 접근 방법:
- 다익스트라 알고리즘을 세 번 실행해 각 구간의 최단 거리를 계산
- 반드시 지나야 하는 정점 v1, v2가 주어질 때 가능한 두 경로:
  1 → v1 → v2 → N  
  1 → v2 → v1 → N  
  두 경로 중 더 짧은 값을 선택
- 세 번의 다익스트라 결과를 조합해서 경로 전체 거리를 계산

느낀점:
- "특정한 정점을 거쳐야 한다"는 조건이 나오면, 다익스트라 여러 번 쓰는 패턴이 자주 등장함
- 문제를 부분 경로로 나누어 각각을 따로 계산하고 합치는 방식이 깔끔하게 적용되었음
- 무작정 최단 경로 하나로 묶지 않고, 분해해서 접근하는 습관이 중요하다고 느낌
"""
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, graph, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    queue = [(0, start)]  # (거리, 노드)

    while queue:
        current_dist, current_node = heapq.heappop(queue)
        if current_dist > dist[current_node]:
            continue
        for next_node, weight in graph[current_node]:
            new_dist = current_dist + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(queue, (new_dist, next_node))
    return dist

def main():
    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, input().split())

    dist_from_1 = dijkstra(1, graph, n)
    dist_from_v1 = dijkstra(v1, graph, n)
    dist_from_v2 = dijkstra(v2, graph, n)

    path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
    path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

    result = min(path1, path2)
    print(result if result < float('inf') else -1)

if __name__ == "__main__":
    main()
