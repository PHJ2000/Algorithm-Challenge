"""
사이트: 백준  
문제 이름: [파이프 옮기기 1](https://www.acmicpc.net/problem/17070)

풀이 접근 방법:
- DP 3차원 배열을 이용해 각 위치에 도달하는 경우의 수를 저장
- dp[y][x][d] : 파이프의 끝이 (y,x)에 있고, 방향이 d일 때의 경우의 수 (0: 가로, 1: 세로, 2: 대각선)
- 상태 전이는 방향에 따라 이전 위치에서 오는 경우를 누적
  - 가로: ←에서 가로 또는 대각선
  - 세로: ↑에서 세로 또는 대각선
  - 대각선: ↖에서 가로/세로/대각선 가능, 단 주변 3칸이 모두 0이어야 함

느낀점:
- 방향성과 조건이 함께 엮인 DP 문제로, 상태 정의를 명확히 하지 않으면 꼬이기 쉬움
- 경우의 수 누적 방식에 익숙해지기에 좋은 문제
"""
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for y in range(N):
    for x in range(2, N):
        if graph[y][x] == 1:
            continue
        dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]
        if y > 0:
            dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]
            if graph[y-1][x] == 0 and graph[y][x-1] == 0 and graph[y-1][x-1] == 0:
                dp[y][x][2] = sum(dp[y-1][x-1])

print(sum(dp[N-1][N-1]))
