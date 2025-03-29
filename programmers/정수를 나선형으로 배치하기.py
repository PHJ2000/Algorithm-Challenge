"""
사이트: 프로그래머스
문제 이름: [정수를 나선형으로 배치하기](https://school.programmers.co.kr/learn/courses/30/lessons/181832)

풀이 접근 방법:
- 먼저 쓰일 공간을 만든 후, 방향을 위해 리스트 2개 생성, 그 후 범위에 벗어나거나, 채워져 있으면 방향 전환을 합니다.

느낀점:
- 생각보다, 바로 구현에 시간이 걸렸다.
"""
def solution(n):
    # n x n 배열 생성 (모두 0으로 초기화)
    board = [[0] * n for _ in range(n)]
    
    # 방향: 오른쪽 → 아래 ↓ 왼쪽 ← 위 ↑
    dx = [0, 1, 0, -1]  # 행 이동
    dy = [1, 0, -1, 0]  # 열 이동
    direction = 0  # 처음엔 오른쪽 방향
    
    x, y = 0, 0  # 시작 위치
    for i in range(1, n * n + 1):
        board[x][y] = i  # 현재 위치에 숫자 채우기
        # 다음 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 다음 위치가 범위를 벗어나거나 이미 숫자가 채워진 경우 → 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
        
        x, y = nx, ny  # 다음 위치로 이동
    
    return board
