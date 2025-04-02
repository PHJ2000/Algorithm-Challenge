"""
사이트: 프로그래머스
문제 이름: [두 정수 사이의 합](https://school.programmers.co.kr/learn/courses/30/lessons/12912)

풀이 접근 방법:
- a,b의 대소관계가 정해져 있지 않으므로, a,b에 대소 관계 파악후 sum과 제너레이터 표현식으로 구현

느낀점:
- 처음에 음수에서 양수로, 양수에서 음수로, 음수에서 음수로 잘 되지 않을까 했지만 올바르게 작동함을 확인하였다.
"""
def solution(a, b):
    if a>b:
        return sum(i for i in range(b,a+1))
    else:
        return sum(i for i in range(a,b+1))
    
"""
좋은 풀이
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))
"""
