"""
사이트: 프로그래머스
문제 이름: [qr code](https://school.programmers.co.kr/learn/courses/30/lessons/181903)

풀이 접근 방법:
- 슬라이싱 기법을 이용하여 간단하게 풀었다

느낀점:
- 슬라이싱은 정말 좋은 기법이다.
"""
def solution(q, r, code):
    return code[r::q]
