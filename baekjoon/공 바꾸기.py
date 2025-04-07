"""
사이트: 백준
문제 이름: [공 바꾸기](https://www.acmicpc.net/problem/10813)

풀이 접근 방법:
- 입출력과 파이썬 특유의 교환방식으 이용하였다.

느낀점:
- 무난하게 풀었다.
"""
n , m = map(int, input().split())
l=[i for i in range(1,n+1)]
for i in range(m):
    a,b = map(int,input().split())
    l[a-1], l[b-1] = l[b-1], l[a-1]
print(*l)
