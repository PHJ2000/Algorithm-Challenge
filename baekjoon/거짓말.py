"""
사이트: 백준  
문제 이름: [거짓말](https://www.acmicpc.net/problem/1043)

풀이 접근 방법:
- 분리 집합(Union-Find)을 활용해 사람들을 그룹으로 묶음
- 진실을 아는 사람과 같은 그룹에 속한 사람은 거짓말을 할 수 없음
- 각 파티를 탐색하면서, 그 안에 진실을 아는 사람과 같은 그룹에 속한 사람이 없다면 거짓말 가능
- 핵심 로직: 각 파티에서 모든 참가자가 진실 그룹과 분리되어 있는지를 확인

느낀점:
- 분리 집합을 활용한 사람 간 관계 연결이 직관적으로 이해됨
- 유니온-파인드 알고리즘의 실전 활용 예제로 좋은 문제
"""
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

n, m = map(int, input().split())
truth = list(map(int, input().split()))
truth = truth[1:]  # 맨 앞은 진실을 아는 사람 수

parent = [i for i in range(n + 1)]
parties = []

for _ in range(m):
    party = list(map(int, input().split()))
    members = party[1:]  # 첫 번째는 인원 수
    for i in range(len(members) - 1):
        union(members[i], members[i + 1])
    parties.append(members)

truth_roots = set(find(x) for x in truth)

ans = 0
for party in parties:
    if all(find(p) not in truth_roots for p in party):
        ans += 1

print(ans)
