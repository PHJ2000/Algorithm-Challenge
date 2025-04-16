"""
사이트: 백준
문제 이름: [체스의 빈칸 칠하기](https://www.acmicpc.net/problem/1018)

풀이 접근 방법:
- 보드에서 가능한 영역을 모두 탐색, 각 구간에 대해, 시작 색이 'W'인 경우와 'B'인 경우를 모두 고려하여 몇 칸을 다시 칠해야 하는지 계산
- 두 경우 중 더 적게 칠하는 경우 선택
느낀점:
- 규칙적인 패턴을 처리할 때는 수학적인 규칙성((i + j) % 2)을 활용하면 구현이 깔끔해짐
- 브루트포스 문제라도 "모든 경우를 확인하는 것"에 집중하면 복잡하지 않게 풀 수 있다
"""
N, M = map(int, input().split())
board = [input() for _ in range(N)]

def repaint_count(x, y, start_color):
    count = 0
    for i in range(8):
        for j in range(8):
            # 체스판 규칙에 따라 색상 계산
            expected_color = start_color if (i + j) % 2 == 0 else ('B' if start_color == 'W' else 'W')
            if board[x + i][y + j] != expected_color:
                count += 1
    return count

min_paint = 64  # 최대는 8*8 = 64
for i in range(N - 7):  # 행
    for j in range(M - 7):  # 열
        # 두 경우 중 최소 칠해야 하는 수
        min_paint = min(min_paint, repaint_count(i, j, 'W'), repaint_count(i, j, 'B'))

print(min_paint)
