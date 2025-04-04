"""
사이트: 백준
문제 이름: [문자열](https://www.acmicpc.net/problem/1120)

풀이 접근 방법:
- f-string을 이용해서 구현

느낀점:
- f 스트링을 활용하는게, 아직 익숙치 않아 헤맸다.
"""
n=int(input())
for i in range(n):
    s=input()
    print(f"{s[0]}{s[-1]}")
