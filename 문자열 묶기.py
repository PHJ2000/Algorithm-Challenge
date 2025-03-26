"""
문제: 프로그래머스 - 문자열 묶기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181855

풀이 방법:
- map을 통하여 리스트에 값을 길이로 바꾼 후에 카운터를 이용해서 해결하였다

어려웠던 점:
- 처음에는 Counter().most_common(1)이 벨류값을 리턴할 줄 알았으나, 이중 리스트 형태로 리턴하여 당황하였다.
"""
from collections import Counter
def solution(strArr):
    strArr = map(len, strArr)
    return Counter(strArr).most_common(1)[0][1]

"""
def solution(strArr):
    d = {}

    for i in strArr:
        d[len(i)] = d.get(len(i), 0) + 1

    return max(d.values())
딕셔너리를 활용한 괜찮은 풀이
"""
