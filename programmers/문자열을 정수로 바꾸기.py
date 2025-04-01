"""
사이트: 프로그래머스
문제 이름: [문자열을 정수로 바꾸기](https://school.programmers.co.kr/learn/courses/30/lessons/12925)

풀이 접근 방법:
- 부호가 -일 때만 -변환을 해주고, 나머지는 int함수를 이용해서 해결

느낀점:
- 숏코딩으로 int만 넣은 것도 보았지만 이렇게 푸는게, 문제를 그대로 구현한 것 같다.
"""
def solution(s):
    if s[0]=='-':
        return -int(s[1:])
    return int(s)
