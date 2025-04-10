"""
사이트: 백준
문제 이름: [N과 M (5)]](https://www.acmicpc.net/problem/15654)

풀이 접근 방법:
- 두번쨰 입력을 정렬 후 순열로 해결, 처음에는 조합인 줄 알았다.
느낀점:
- itertools 라이브러리가 있어서 참 다행이다. 빠르게 익숙해지면 좋겠다.
- 
"""
from itertools import permutations
N, M = map(int,input().split())
l=sorted(map(int, input().split()))
for i in permutations(l,M):
    print(*i)
