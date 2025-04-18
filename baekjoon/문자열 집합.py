"""
사이트: 백준
문제 이름: [문자열 집합](https://www.acmicpc.net/problem/14425)

풀이 접근 방법:
- set을 이용해서 &연산으로 문제 해결히라 헸으나, 입출력에서 문제를 맞다트리고, readline과 strip을 이용하여 해결

느낀점:
- input()이 불완전하게 입력을 받는 줄은 몰랐다. strip을 열심히 써보자.
"""
import sys

N, M = map(int, sys.stdin.readline().split())
s = set(sys.stdin.readline().strip() for _ in range(N))

cnt = 0
for _ in range(M):
    word = sys.stdin.readline().strip()
    if word in s:
        cnt += 1

print(cnt)
