"""
사이트: 프로그래머스
문제 이름: [약수의 합](https://school.programmers.co.kr/learn/courses/30/lessons/12928)

풀이 접근 방법:
- 반복문을 이용해서, 약수를 모두 더해서 구현

느낀점:
- num/2의 수만 검사하는 방식으로 성능을 늘리다니 너무 신기하다.
"""
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer+=i
    return answer

"""
좋은 풀이
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
"""
