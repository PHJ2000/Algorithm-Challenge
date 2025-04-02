"""
사이트: 프로그래머스
문제 이름: [정수 제곱근 판별](https://school.programmers.co.kr/learn/courses/30/lessons/12934)

풀이 접근 방법:
- math.sqrt를 활용하여 문제 해결, 부동소수점 문제를 완화하기 위해 int사용

느낀점:
- 부동소수점 문제를 고려하는 게 중요함을 느꼈다. 완전히 무결한 코드랑, 보정 코드도 찾아보니 새로웠다.
"""
from math import sqrt
def solution(n):
    if int(sqrt(n))**2==n:
        return int(sqrt(n)+1)**2
    return -1

"""
좋은 풀이
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
    
def nextSquare(n):
    sqrt = int(n ** 0.5 + 1e-10)  # 부동소수점 보정
    if sqrt * sqrt == n:
        return (sqrt + 1) ** 2
    return 'no'
    
import math

def nextSquare(n):
    sqrt = math.isqrt(n)
    if sqrt ** 2 == n:
        return (sqrt + 1) ** 2
    return 'no'
"""
