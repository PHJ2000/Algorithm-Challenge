"""
사이트: 프로그래머스
문제 이름: [커피 심부름](https://school.programmers.co.kr/learn/courses/30/lessons/181837)

풀이 접근 방법:
- 결국에 최종 금액을 리턴하는 것이므로, 아메리카노인지, 카페라떼인지만 중요함
- anything을 포함여서 in 연산자로 해결

느낀점:
- 문제 설명을 꼬아놓아도 핵심만 파악하면 간단하게 풀 수 있음을 알았다.
"""
def solution(order):
    answer = 0
    for o in order:
        if "americano" in o or "anything" in o:
            answer+=4500
        if "cafelatte" in o:
            answer+=5000
    return answer
