"""
사이트: 백준
문제 이름: [가장 긴 부분 수열]](https://www.acmicpc.net/problem/11053)

풀이 접근 방법:
- 처음에 dp가 떠올랐지만, 해결법이 생각나지 않아, 백트래킹으로 할 생각을 하였고, 결국에는 dp로 풀었다.

느낀점:
- 백트래킹으로 시도를 할 때, 구현을 하지 못 했다. dp만 너무 익숙하지 않은 지 걱정된다.
- 
"""
N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N  # 자기 자신 하나만으로도 길이 1

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
