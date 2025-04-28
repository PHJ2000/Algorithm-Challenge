"""
사이트: 백준
문제 이름: [스티커](https://www.acmicpc.net/problem/9465)

풀이 접근 방법:
- DP를 활용해 각 열의 최대 점수를 누적
- 점화식: 
    dp[i][0] = sticker[0][i] + max(dp[i-1][1], dp[i-2][1])
    dp[i][1] = sticker[1][i] + max(dp[i-1][0], dp[i-2][0])

느낀점:
- 이전 선택이 현재 선택에 미치는 영향을 생각하며 최적의 경로를 찾는 연습이 됨
"""
t = int(input())

for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue

    dp = [[0]*n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = sticker[0][1] + dp[1][0]
    dp[1][1] = sticker[1][1] + dp[0][0]

    for i in range(2, n):
        dp[0][i] = sticker[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = sticker[1][i] + max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))
