"""
1. 뭘 해야 하는가?

제약:
- 좌측 상단 (0,0)에 말이 놓여 있음
- 상하좌우로 이동 가능
- 이동한 알파벳과 같은 알파벳은 다시 밟을 수 없음
- 표 모양 보드(R, C), 1 <= R, C <= 20

입력:
- 세로 R, 가로 C
- R개 줄에 걸쳐 C개의 대문자 알파벳이 빈칸 없이 주어짐

출력:
- 말이 지날 수 있는 최대 칸 수를 출력

2. 입력/제약 → 알고리즘 도출

- 표 형식 문제 + 중복 없는 문자열 조건 → 경로 탐색 문제
- 같은 알파벳은 한 번만 밟을 수 있으므로, 최대 26칸까지 가능
- 최장 경로를 찾아야 하므로 DFS + 백트래킹이 적절
- PyPy 기준에서 set 대신 **비트마스킹**으로 방문 여부 체크해야 통과 가능
- DFS 중 현재 알파벳을 비트로 체크하고, 백트래킹 시 비트 제거 없이 넘김 (값만 넘김)

3. 중간/최종/로직

- 최종 목표: 가능한 경로 중 알파벳 중복 없이 가장 많이 밟은 칸 수의 최대값
- 상태: 현재 위치 (x, y), 방문한 알파벳 비트마스크, 현재까지 이동한 거리 (depth)
- 전역 변수 max_len으로 최댓값을 갱신
- 종료 조건 없이 모든 분기 탐색 (26칸이 최대)

4. 테스트 케이스

전부 같은 알파벳: 1칸만 이동 가능
입력:
2 2  
AA  
AA  
출력:  
1

전부 다른 알파벳: 26칸 이동 가능
입력:
2 13  
ABCDEFGHIJKLM  
NOPERSTUWVXYZ  
출력:  
26

일반적인 경우
입력:
3 3  
ABA  
CJK  
IBZ  
출력:  
7

"""
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_len = 0

def dfs(x, y, visited, depth):
    global max_len
    max_len = max(max_len, depth)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            idx = ord(board[nx][ny]) - ord('A')
            if not (visited & (1 << idx)):
                dfs(nx, ny, visited | (1 << idx), depth + 1)

start = ord(board[0][0]) - ord('A')
dfs(0, 0, 1 << start, 1)
print(max_len)
