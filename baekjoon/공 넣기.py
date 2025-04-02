"""
사이트: 백준
문제 이름: [공 넣기](https://www.acmicpc.net/problem/10810)

풀이 접근 방법:
- 리스트 슬라이싱을 이용해서 문제를 해결하였습니다.

느낀점:
- 프로그래머스로 풀다가 백준으로 푸니, map(int, input().split())이 익숙하지가 않다.
- 백준에서는 리스트 출력이 아닌 공백으로 구분된 출력이 필요하다는 점을 기억해야겠다.
- 입출력 형식에 주의하는 습관을 들여야겠다.
"""
N, M = map(int,input().split())
l=[0]*N
for i in range(M):
    s,e,n = map(int,input().split())
    l[s-1:e]=[n]*(e-s+1)
print(*l)

"""
해당 코드가 inplace방식이고, 위에 코드가 새로운 리스트를 만드는 형식이라, 약간의 차이로 이 코드가 더 좋음
N, M = map(int, input().split())

arr = [0] * N

for i in range(M):
  i,j,k = map(int, input().split())
  for b in range(i-1,j):
    arr[b] = k
    
print(*arr)
"""
