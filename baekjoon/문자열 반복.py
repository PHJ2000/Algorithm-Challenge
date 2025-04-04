"""
사이트: 백준
문제 이름: [문자열 반복](https://www.acmicpc.net/problem/2675)

풀이 접근 방법:
- 반복문과 문자 연산을 이용해서 구현함

느낀점:
- 문제를 잘 못 읽어서, 전체를 반복했었다. 주의 깊게 읽어야겠다.
"""
n = int(input())
for _ in range(n):
    m, s = input().split()
    m = int(m)
    result = ""
    for char in s:
        result += char * m
    print(result)
