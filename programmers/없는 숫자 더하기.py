"""
사이트: 프로그래머스
문제 이름: [없는 숫자 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/86051)

풀이 접근 방법:
- 중복이 허용되지 않고, 지정된 수만 있으므로 수학적으로 접근하였다.

느낀점:
- 깔끔하게 잘 푼 듯하다.
"""
def solution(numbers):
    return 45-sum(numbers)


"""
좋은 풀이
solution = lambda x: sum(range(10)) - sum(x)
"""
