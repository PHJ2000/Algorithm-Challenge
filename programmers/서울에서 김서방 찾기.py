"""
사이트: 프로그래머스
문제 이름: [서울에서 김서방 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/12919)

풀이 접근 방법:
- enumerate와 f-string을 활용하여 문제를 품

느낀점:
- index라는 좋은 내부 함수를 기억 못하고 있었다. 좀 더 자주 활용해야겠다.
"""
def solution(seoul):
    for idx,name in enumerate(seoul):
        if name == "Kim":
            return f"김서방은 {idx}에 있다"
        
"""
좋은 풀이
return "김서방은 {}에 있다".format(seoul.index('Kim'))
"""
