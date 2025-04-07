"""
사이트: 백준
문제 이름: [킹, 퀸, 룩, 비숍, 나이트, 폰](https://www.acmicpc.net/problem/3003)

풀이 접근 방법:
- 빼기를 이용하여 구현

느낀점:
- .format이 익숙하다 보니 f-string을 연습할 수 있는 좋은 기회가 되었다.
"""
k, q, r, b, n, p = map(int, input().split())
print(f"{1-k} {1-q} {2-r} {2-b} {2-n} {8-p}")

"""
좋은 풀이
standard = [1, 1, 2, 2, 2, 8]
current = list(map(int, input().split()))
print(*[s - c for s, c in zip(standard, current)])
"""
