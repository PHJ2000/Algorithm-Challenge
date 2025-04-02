"""
사이트: 프로그래머스
문제 이름: [문자열 내 p와 y의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/12916)

풀이 접근 방법:
- upper()를 이용해서 통일 시킨후, 변수 하나로 카운팅하여 문제 해결

느낀점:
- Counter도 알고는 있었지만 사용법이 익숙하지 않아 단순 구현 했다. 그러나 이제는 알았으니, 다음부터 잘 해내겠다!
"""
def solution(s):
    c=0
    for i in s:
        if i.upper()=='P':
            c+=1
        if i.upper()=='Y':
            c-=1
    return c==0

"""
좋은 풀이
from collections import Counter
def numPY(s):
    # 함수를 완성하세요
    c = Counter(s.lower())
    return c['y'] == c['p'] 
"""
