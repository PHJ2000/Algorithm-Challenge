"""
사이트: 프로그래머스
문제 이름: [음양 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/76501)

풀이 접근 방법:
- 삼항 연산자와 sum, 제너레이터 표현식을 사용하여 해결

느낀점:
- 삼항 연산자가 아직 익수하지 않지만, 쓰고 보니 정말 깔끔하다.
"""
def solution(absolutes, signs):
    answer = sum(nu if sign else -nu for nu, sign in zip(absolutes, signs))
    return answer
