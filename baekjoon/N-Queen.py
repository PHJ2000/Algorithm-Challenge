"""
사이트: 백준  
문제 이름: [N-Queen](https://www.acmicpc.net/problem/9663)

풀이 접근 방법:  
- 백트래킹을 사용해 한 행씩 퀸을 배치하며 유효한 경우만 탐색  
- 조건: 같은 열, 좌상향/우상향 대각선에 퀸이 없도록 체크  
- set 대신 bool 배열(col, 대각선)로 방문 여부를 관리해 시간 복잡도 개선  
- 재귀적으로 모든 유효한 퀸 배치를 탐색하며 경우의 수를 count

느낀점:  
- 백트래킹에서 pruning 조건을 명확히 하는 것이 효율성 향상에 중요하다는 걸 느낌  
- set보다 배열을 써서 성능을 개선하는 팁이 실제로 얼마나 큰 차이를 내는지 체감함  
- 수학적 인덱스 설계(row ± col)를 통한 대각선 표현이 깔끔하고 인상적이었음
"""
import sys
sys.setrecursionlimit(10000)

def solve_n_queens(n):
    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col_used[col] or diag1[row + col] or diag2[row - col + n - 1]:
                continue
            col_used[col] = diag1[row + col] = diag2[row - col + n - 1] = True
            backtrack(row + 1)
            col_used[col] = diag1[row + col] = diag2[row - col + n - 1] = False

    count = 0
    col_used = [False] * n
    diag1 = [False] * (2 * n - 1)  # row + col
    diag2 = [False] * (2 * n - 1)  # row - col + n - 1
    backtrack(0)
    return count

def main():
    n = int(sys.stdin.readline())
    print(solve_n_queens(n))

if __name__ == "__main__":
    main()
