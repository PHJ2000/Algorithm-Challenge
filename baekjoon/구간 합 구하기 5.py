"""
사이트: 백준
문제 이름: [구간 합 구하기 5](https://www.acmicpc.net/problem/11660)

풀이 접근 방법:
- 2차원 누적합(Prefix Sum)을 미리 계산해두고, 쿼리마다 O(1)로 답을 구했다.
- 누적합 배열 S를 정의: S[i][j] = (1,1) ~ (i,j)까지의 합
- S 배열은 다음과 같은 점화식으로 계산:
    - S[i][j] = A[i-1][j-1] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]
- 질의 (x1,y1,x2,y2)에 대해 구간합은:
    - S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1] 로 구함

느낀점:
- 처음에는 1차원 누적합(행별 누적합)만 만들어서 쿼리마다 여러 행을 순회하는 방식으로 구현했으나, 시간초과가 발생했다.
- 이후 2차원 전체 누적합을 구성하고 O(1) 공식으로 구해야 한다는 것을 알게 되었다.
- 또한 Python 기본 input() 사용이 매우 느리다는 것을 체감했고, sys.stdin.readline()으로 입력을 빠르게 처리하는 것이 필수라는 점도 배웠다.
- 문제를 풀면서 입력 처리 속도와 알고리즘 시간복잡도 최적화의 중요성을 모두 깨닫게 되었다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

S = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        S[i][j] = A[i-1][j-1] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    print(ans)
