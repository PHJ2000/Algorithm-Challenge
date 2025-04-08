"""
사이트: 백준
문제 이름: [별 찍기 - 7](https://www.acmicpc.net/problem/2444)

풀이 접근 방법:
- 반복문을 통하여 구현

느낀점:
- 문자열 곱셈이 되니, 곱하여 해결하면 된다는 것을 다시금 깨닫게 되었다.
"""
def print_line(spaces, stars):
    print(" " * spaces + "*" * stars)

n = int(input())

# 위쪽 삼각형
for i in range(n):
    spaces = n - i - 1
    stars = i * 2 + 1
    print_line(spaces, stars)

# 아래쪽 역삼각형
for i in range(n - 1):
    spaces = i + 1
    stars = (n - i - 2) * 2 + 1
    print_line(spaces, stars)
