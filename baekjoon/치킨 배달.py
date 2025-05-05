"""
사이트: 백준  
문제 이름: [치킨 배달](https://www.acmicpc.net/problem/15686)

풀이 접근 방법:
- 치킨집 좌표 중 M개를 조합으로 선택 (combinations)
- 선택된 조합에 대해, 각 집에서 가장 가까운 치킨집까지의 거리 합을 계산
- 모든 조합에 대해 최소 거리 합을 비교하여 정답 도출

느낀점:
- 완전탐색 문제에서 조합을 어떻게 활용할지 체계적으로 연습할 수 있었음
- 거리 계산 로직을 깔끔하게 분리하는 것이 구현 안정성에 도움이 되었음
"""
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

homes = []
chickens = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

min_total_distance = float('inf')

for chicken_comb in combinations(chickens, m):
    total_distance = 0
    for hx, hy in homes:
        dist = min(abs(hx - cx) + abs(hy - cy) for cx, cy in chicken_comb)
        total_distance += dist
    min_total_distance = min(min_total_distance, total_distance)

print(min_total_distance)

