"""
사이트: 백준
문제 이름: [N과 M (9)](https://www.acmicpc.net/problem/15663)

풀이 접근 방법:
- 순열로 만든 다음에, 셋을 이용해서, 중복되는 것을 걸러내어서 해결

느낀점:
- 순열, 조합, 중복 가능 조합에 개념을 명확히 하여, 빠르게 문제를 풀어야겠다.
"""
from itertools import permutations
N, M = map(int,input().split())
l=sorted(list(map(int,input().split())))
s=set()
for i in permutations(l,M):
    if i not in s:
        s.add(i)
        print(*i)
