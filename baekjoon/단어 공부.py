"""
사이트: 백준
문제 이름: [단어 공부](http://acmicpc.net/problem/1157)

풀이 접근 방법:
- Counter를 활용하여 처리, 대소문자 구분을 안하므로 upper로 통일

느낀점:
- most_common결과 값을 인덱스로 접근 가능하다는 것을 알았다.
"""
from collections import Counter
s=input().upper()
v=Counter(s).most_common(2)
if len(v)>=2 and v[0][1]==v[1][1]:
    print("?")
else:
    print(v[0][0])
