"""
사이트: 백준
문제 이름: [N과 M (4)](https://www.acmicpc.net/problem/15652)

풀이 접근 방법:
- 중복 조합 라이브러리를 사용하여 해결

느낀점:
- 중복 조합 라이브러리가 기억이 안나 곤혹스러웠으며, 백트래킹으로 푸는게 익숙하지 않아
- 백트래킹으로 푸는 데 실패했다.
"""
from itertools import combinations_with_replacement
M,N = map(int, input().split())
answer=[]
for i in combinations_with_replacement(range(1,M+1),N):
    print(*i)

"""
백트래킹 풀이
n, m = map(int, input().split())

def backtrack(start, path):
    if len(path) == m:
        print(*path)
        return
    for i in range(start, n + 1):
        backtrack(i, path + [i])

backtrack(1, [])
"""
