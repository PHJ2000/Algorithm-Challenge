"""
사이트: 백준
문제 이름: [단어의 개수](https://www.acmicpc.net/problem/1152)

풀이 접근 방법:
- split과 len을 이용해서 구현함

느낀점:
- 공백을 가지고 단어를 구분하여 진행하였다. 딱 깔끔하게 되어 기분이 좋았다.
"""
n=input()
print(len(n.split()))
