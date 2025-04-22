"""
사이트: 백준  
문제 이름: [N과 M (1)](https://www.acmicpc.net/problem/15649)

풀이 접근 방법:
- 백트래킹(DFS)을 이용해 길이가 M인 순열을 생성
- 1부터 N까지의 수를 중복 없이 선택
- visited 배열을 활용하여 중복 방지
- 수열 완성 시 출력 후 백트래킹으로 되돌아감

느낀점:
- DFS의 흐름과 백트래킹 구조에 대한 이해가 깊어짐
- 반복문과 재귀의 조합을 통해 문제를 어떻게 탐색할 수 있는지 실전적으로 익힘
"""
N, M = map(int, input().split())
visited = [False] * (N + 1)
result = []

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(depth + 1)
            result.pop()
            visited[i] = False

dfs(0)
