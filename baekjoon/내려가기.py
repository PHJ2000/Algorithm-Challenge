"""
사이트: 백준
문제 이름: [내려가기](https://www.acmicpc.net/problem/2096)

풀이 접근 방법:
- 얻을 수 있는 최대 점수와 최소점수, dp를 이용하면 된다.
- dp[i][j]=max(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
- dpm을 만들어 동일하게 적용하면 된다.
- 그러나, 메모리 문제로 메모리 부족이 발생하였다.
- 이에, 전에 값만 알고 있으면 된다는 것에 착안해서 O(N)->O(1)으로 줄이는데 성공했다.

느낀점:
- 접근 자체는 좋았지만, 메모리 제약을 확인하지 않고 진행하여, 첫 채점에서 틀렸다. 보다 상세히 확인해야겠다.
"""
import sys
input = sys.stdin.readline

N = int(input())
prev_max = [0] * 3
prev_min = [0] * 3

for i in range(N):
    a, b, c = map(int, input().split())
    if i == 0:
        prev_max = [a, b, c]
        prev_min = [a, b, c]
    else:
        curr_max = [
            a + max(prev_max[0], prev_max[1]),
            b + max(prev_max[0], prev_max[1], prev_max[2]),
            c + max(prev_max[1], prev_max[2])
        ]
        curr_min = [
            a + min(prev_min[0], prev_min[1]),
            b + min(prev_min[0], prev_min[1], prev_min[2]),
            c + min(prev_min[1], prev_min[2])
        ]
        prev_max = curr_max
        prev_min = curr_min

print(max(prev_max), min(prev_min))
