"""
사이트: 백준  
문제 이름: [숨바꼭질 3](https://www.acmicpc.net/problem/13549)

풀이 접근 방법:
- 순간이동(*2)은 0초, 걷기(+1/-1)는 1초가 걸리는 가중치가 다른 그래프
- 이를 해결하기 위해 0-1 BFS를 사용
- 덱을 활용해 순간이동은 앞쪽에 넣고, 걷기는 뒤쪽에 넣음
- visited 리스트는 각 위치까지 도달하는 데 걸린 최소 시간을 기록
- 처음에는 float('inf')로 초기화해 방문 여부 및 최소값 갱신을 쉽게 구현
- 목표 지점에 처음 도달하면 그 시간이 정답

느낀점:
- 가중치가 다른 경로 탐색 문제에서 0-1 BFS의 효율성을 체감함
- 우선순위 큐 없이도 시간 복잡도를 낮출 수 있다는 점이 인상 깊었음
"""
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
limit = max(N, K) * 2 + 1
m = [float('inf')] * limit  # 방문 시간(초) 저장
m[N] = 0  # 시작점 시간 0
d = deque()
d.append(N)

while d:
    p = d.popleft()

    if p == K:
        print(m[p])
        break

    # 순간이동 (비용 0) → 덱 앞에 넣기
    if p * 2 < limit and m[p * 2] > m[p]:
        m[p * 2] = m[p]
        d.appendleft(p * 2)

    # -1 이동 (비용 1)
    if p > 0 and m[p - 1] > m[p] + 1:
        m[p - 1] = m[p] + 1
        d.append(p - 1)

    # +1 이동 (비용 1)
    if p + 1 < limit and m[p + 1] > m[p] + 1:
        m[p + 1] = m[p] + 1
        d.append(p + 1)
