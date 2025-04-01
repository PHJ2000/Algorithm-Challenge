"""
사이트: 백준
문제 이름: [영수증](https://www.acmicpc.net/problem/25304)

풀이 접근 방법:
- 간단한 구현 문제다, 입력을 map을 이용해서 처리하였다.

느낀점:
- map을 활용해서 입출력을 하니 한결 편하다.
"""
X=int(input())
N=int(input())
price=0
for i in range(N):
    a, b = map(int, input().split())
    price+=a*b
if price==X:
    print("Yes")
else:
    print("No")
