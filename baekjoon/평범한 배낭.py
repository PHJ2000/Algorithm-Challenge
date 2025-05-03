"""
사이트: 백준  
문제 이름: [평범한 배낭](https://www.acmicpc.net/problem/12865)

풀이 접근 방법:
- 중복 없이 물건을 선택하는 0/1 Knapsack 문제
- dp[w] = 무게 w일 때 얻을 수 있는 최대 가치
- 한 물건을 여러 번 선택하지 않기 위해 무게 역순으로 dp 배열을 갱신
- 점화식: dp[w] = max(dp[w], dp[w - weight] + value)

느낀점:
- 단순히 모든 조합을 생각하면 시간 초과가 나는 것을 몸소 느꼈다
- 갱신 순서(역순 vs 정순)에 따라 중복 선택이 생길 수 있다는 걸 처음 알았다
- 상태 전이와 dp 배열의 의미를 직접 손으로 써보며 구조를 파악한 것이 큰 도움이 되었다
"""
import sys
input = sys.stdin.readline

# 입력
N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i] = 무게 i일 때 최대 가치
dp = [0] * (K + 1)

for weight, value in items:
    for w in range(K, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[K])
