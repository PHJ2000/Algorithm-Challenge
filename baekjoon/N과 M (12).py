"""
사이트: 백준
문제 이름: [N과 M (12)](https://www.acmicpc.net/problem/15666)

풀이 접근 방법:
- 중복조합과 집합을 이용해서 풀이이

느낀점:
- 저번에 풀었던 문제와 유사해서 편하게 풀었다.

"""
from itertools import combinations_with_replacement
N, M = map(int,input().split())
l=sorted(list(map(int,input().split())))
s=set()
for i in combinations_with_replacement(l,M):
    if i not in s:
        s.add(i)
        print(*i)
