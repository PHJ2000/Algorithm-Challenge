"""
문제: 프로그래머스 - 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181872

풀이 방법:
- range에서 거꾸로 나오게 진행을 해서, 하나만 찾게 되면 처음부터 해당 위치까지 슬라이싱하여 품

어려웠던 점:
- 거꾸로 진행되게 할 때, 두 번째 파라미터가 0이 아닌 -1로 해야하는 점이 헷갈렸음
"""
def solution(myString, pat):
    answer = ''
    np=len(pat)
    for i in range(len(myString)-np,-1,-1):
        if myString[i:i+np]==pat:
            return myString[0:i+np]
