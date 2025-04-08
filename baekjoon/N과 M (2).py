"""
사이트: 백준
문제 이름: [N과 M (2)](https://www.acmicpc.net/problem/15650)

풀이 접근 방법:
- 조합을 이용하여 해결하였다.

느낀점:
- itertools는 정말 최고의 라이브러리다.
"""
from itertools import combinations

n, m = map(int, input().split())
for seq in combinations(range(1, n + 1), m):
    print(*seq)
