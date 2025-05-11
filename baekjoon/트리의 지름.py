"""
사이트: 백준  
문제 이름: [트리의 지름](https://www.acmicpc.net/problem/1967)

풀이 접근 방법:
- DFS를 두 번 수행해 트리의 지름을 구함
- 첫 DFS: 임의의 노드(1번)에서 가장 멀리 있는 노드를 찾음
- 두 번째 DFS: 찾은 노드에서 가장 멀리 떨어진 노드까지의 거리 → 트리의 지름

느낀점:
- 트리는 사이클이 없다는 특성 덕분에, 임의 노드에서 시작해 두 번 DFS만으로 지름을 쉽게 구할 수 있다는 점이 인상 깊었음  
- 재귀 호출이 깊어질 수 있어 `sys.setrecursionlimit` 조절이 필요했음  
- 트리의 지름이라는 개념이 알고리즘 대회나 코딩 테스트에서 자주 등장하므로 반드시 익혀둘 만한 유형
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    tree[a].append((b, w))
    tree[b].append((a, w))

def dfs(node, weight):
    for next_node, w in tree[node]:
        if visited[next_node] == -1:
            visited[next_node] = weight + w
            dfs(next_node, weight + w)

visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)
start = visited.index(max(visited))

visited = [-1] * (n + 1)
visited[start] = 0
dfs(start, 0)
print(max(visited))
