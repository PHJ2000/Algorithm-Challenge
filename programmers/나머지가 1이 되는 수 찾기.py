"""
사이트: 프로그래머스
문제 이름: [나머지가 1이 되는 수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/87389)

풀이 접근 방법:
- 문제에서 설명해준 대로 그대로 구현하였다.

느낀점:
- 이렇게 하는 것이 가장 깔끔하다.
"""
def solution(n):
    for i in range(2,n):
        if n%i==1:
            return i
