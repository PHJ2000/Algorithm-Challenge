"""
사이트: 백준
문제 이름: [바구니 뒤집기](https://www.acmicpc.net/submit/10811)

풀이 접근 방법:
- [:][::-1]을 활용하여 뒤집어서 구현함

느낀점:
- 백준에 점점 익숙해지는 것 같다.
"""
N, M = map(int, input().split())
arr=[i for i in range(1,N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a-1:b]=arr[a-1:b][::-1]
print(*arr)
