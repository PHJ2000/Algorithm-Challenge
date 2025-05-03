"""
사이트: 백준
문제 이름: [LCS](https://www.acmicpc.net/problem/9251)

풀이 접근 방법:
- 두 문자열의 각 문자를 비교하며 부분 수열을 확장하는 방식으로 접근
- 이전까지의 최장 공통 부분 수열 길이를 저장하면서 누적 계산
- 같은 문자가 등장하면 이전 상태에서 +1, 다르면 이전 결과 중 최대값을 선택
- 2차원 DP 테이블을 활용해 중복 계산을 피하고 효율적으로 해결

느낀점:
- 문자열 비교 과정을 시각적으로 단계별로 추적하는 연습이 많이 되었음
- 무식한 방식이 아닌, 누적과 재사용의 사고가 문제 해결에 핵심임을 체감
"""
def lcs(a: str, b: str) -> int:
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

# 입력 예시
a = input().strip()
b = input().strip()
print(lcs(a, b))