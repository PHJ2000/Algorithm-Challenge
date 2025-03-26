"""
문제: 프로그래머스 - 2의 영역
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181894

풀이 방법:
- 양 끝에서 2를 찾고, 그 범위에 해당하는 리스트를 리턴

어려웠던 점:
- 처음에는 range를 두 개 쓴다음 zip으로 묶었으나 if first == -1이 더 편한 것을 알았다.
"""

def solution(arr):
    first = -1
    last = -1
    if 2 not in arr:
        return [-1]
    
    for i, num in enumerate(arr):
        if num == 2:
            if first == -1:
                first = i
            last = i

    return arr[first:last+1]
