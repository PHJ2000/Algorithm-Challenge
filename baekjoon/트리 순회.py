"""
사이트: 백준
문제 이름: [트리 순회](https://www.acmicpc.net/problem/1991)

풀이 접근 방법:
- 트리를 딕셔너리 형태로 저장 (각 노드마다 왼쪽, 오른쪽 자식 기록)
- 전위 순회(Preorder), 중위 순회(Inorder), 후위 순회(Postorder)를 재귀로 구현
- 각각 순회의 정의에 맞게 출력 순서를 조정
  - 전위 순회: 루트 → 왼쪽 → 오른쪽
  - 중위 순회: 왼쪽 → 루트 → 오른쪽
  - 후위 순회: 왼쪽 → 오른쪽 → 루트

느낀점:
- 트리 구조를 입력받고 저장하는 방법을 연습할 수 있었음
- 각각의 순회 방법을 명확히 이해하고, 재귀 함수로 깔끔하게 구현하는 게 중요하다는 걸 느꼈음
- 재귀 호출의 순서가 결과에 직접적으로 반영되기 때문에, 순서를 신중하게 짜야 한다는 걸 다시 한번 깨달음
"""
import sys
input = sys.stdin.read

def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])

def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')

data = input().splitlines()
n = int(data[0])
tree = {}

for i in range(1, n+1):
    root, left, right = data[i].split()
    tree[root] = (left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')
