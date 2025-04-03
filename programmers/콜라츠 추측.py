"""
사이트: 프로그래머스
문제 이름: [콜라츠 추측](https://school.programmers.co.kr/learn/courses/30/lessons/12943)

풀이 접근 방법:
- 단순히 구현하였습니다.

느낀점:
- 이런 문제는 묵묵히 구현하는 방법밖에 떠오르지 않네요.
"""
def solution(num):
    answer=0
    while num!=1:
        if num%2==0:
            num/=2
        else:
            num=num*3+1
        answer+=1
        if answer>500:
            return -1
    return answer
