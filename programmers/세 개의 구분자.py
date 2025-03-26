"""
문제: 프로그래머스 - 세 개의 구분자
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181862

풀이 방법:
- 정규식을 통해서, 스플릿을 보다 효율적으로 사용하고, 빈 문자열을 제거해주었다.

어려웠던 점:
- 처음에는 정규식을 생각하지 못해서 3번 split을 적용하였으나, 정답이 아니어서 힘들었다.
"""
"""
정규식으로 되니 기분이 매우 좋다.
"""
import re
def solution(myStr):
    
    # "a", "b", "c"를 구분자로 나눕니다.
    parts = re.split('[abc]', myStr)
    
    # 빈 문자열을 제거합니다.
    result = [part for part in parts if part]
    
    # 결과가 비어 있다면 ["EMPTY"] 반환
    return result if result else ["EMPTY"]

"""
def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']
정말 좋은 아이디어다
"""
