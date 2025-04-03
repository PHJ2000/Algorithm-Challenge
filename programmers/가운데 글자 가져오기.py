"""
사이트: 프로그래머스
문제 이름: [가운데 글자 가져오기](https://school.programmers.co.kr/learn/courses/30/lessons/12903)

풀이 접근 방법:
- 분기와 슬라이싱을 통해서 구현함

느낀점:
- 분기 없이 슬라이싱으로 해결하다니 대단하네요.
"""
def solution(s):
    if len(s)%2==1:
        return s[len(s)//2]
    else:
        return s[len(s)//2-1:len(s)//2+1]

"""
좋은 풀이
return str[(len(str)-1)//2 : len(str)//2 + 1]
"""
