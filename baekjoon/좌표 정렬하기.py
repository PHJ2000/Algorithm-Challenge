"""
사이트: 백준
문제 이름: [좌표 정렬하기](https://www.acmicpc.net/problem/11650)

풀이 접근 방법:
- sort에 람다식을 활용하여 문제를 풀었다.

느낀점:
- 처음에, 람다값 두 개를 지정하니 오류가 떠서 당황했지만, 묶어서 하니 되었다.
- list와 map을 활용하여 한 번에 리스트를 만드는 방식 배워야겠다.
"""
N = int(input())
l=[]
for i in range(N):
    a,b = map(int, input().split())
    l.append([a,b])
l.sort(key=lambda x: (x[0],x[1]))
for i in l:
    print(*i)

"""
N = int(input())  # 좌표 개수 입력
coords = [list(map(int, input().split())) for _ in range(N)]  # 좌표 입력 받아 리스트에 저장

# x 오름차순, x가 같으면 y 오름차순 정렬
coords.sort(key=lambda x: (x[0], x[1]))

# 정렬된 좌표 출력
for x, y in coords:
    print(x, y)
"""
