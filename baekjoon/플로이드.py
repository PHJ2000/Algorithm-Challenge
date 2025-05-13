"""
1. 무엇을 내야 하는가?
- 입력: 도시의 개수 N (2 <= N <= 100), 버스의 개수 M (1 <= M <= 100000)
- 각 버스 노선은 (시작 도시 a, 도착 도시 b, 비용 c) 형태로 주어진다.
- 출력: N개의 줄에 걸쳐, i번째 줄의 j번째 숫자는 i번 도시에서 j번 도시로 가는 최소 비용을 의미한다.
        단, 갈 수 없는 경우 0을 출력한다.

2. 입력/제약 → 알고리즘/자료구조
- 방향성 있는 멀티 그래프에서 모든 정점 쌍 간의 최소 비용을 구하는 문제이다.
- 다익스트라 대신 플로이드-워셜 알고리즘이 적절하다. (시간 복잡도 O(N^3), N <= 100이므로 가능)
- 같은 도시 쌍 사이에 여러 개의 버스 노선이 존재할 수 있으므로, 입력 시 최소 비용만 유지해야 한다.

3. 중간 결과 / 최종 출력 / 연결 로직
- 중간 결과: dist[i][j] = i번 도시에서 j번 도시로 가는 현재까지의 최소 비용
- 최종 결과: dist 배열을 완성한 뒤 출력 단계에서 i→j 비용을 출력
- 연결 로직: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 를 3중 루프로 수행

4. 테스트 케이스 구성
- 모든 도시가 서로 연결된 경우
- 연결되지 않은 도시가 있는 경우
- 동일 도시쌍에 대해 여러 노선이 존재하는 경우 (비용 비교 필수)
- 자기 자신으로 가는 경우는 항상 비용 0 (명시적 처리 필요)
"""
import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if dist[i][j] == INF else dist[i][j], end=' ')
    print()
