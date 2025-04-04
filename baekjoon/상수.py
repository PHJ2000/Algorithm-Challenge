"""
사이트: 백준
문제 이름: [상수](https://www.acmicpc.net/problem/2908)

풀이 접근 방법:
- [::-1]을 이용하여 문자열 뒤집어 문제 해결

느낀점:
- 처음에는 reversed를 활용하고자 했으나, 반복자 판정이기에 int가 안되기에 [::-1] 채택
"""
n, m=input().split()
n = int(n[::-1])
m = int(m[::-1])
if n>m:
    print(n)
else:
    print(m)
