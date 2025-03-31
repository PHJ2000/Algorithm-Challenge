"""
사이트: 
문제 이름: [짝수와 홀수](https://school.programmers.co.kr/learn/courses/30/lessons/12937)

풀이 접근 방법:
- 조건문을 이용하여 해결하였습니다.
- 사용한 알고리즘이나 자료구조

느낀점:
- 조건문으로 간닪게 해결하였다.
"""
def solution(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
