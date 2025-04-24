"""
사이트: 백준  
문제 이름: [동전 0](https://www.acmicpc.net/problem/11047)

풀이 접근 방법:
- 그리디 알고리즘 사용
- 가장 큰 가치의 동전부터 가능한 최대한 사용
- 현재 금액 K에서 해당 동전으로 만들 수 있는 수만큼 빼며 동전 수 누적

느낀점:
- 탐욕법의 기초를 익힐 수 있는 좋은 문제
- 왜 그리디가 최적해를 보장하는지 이유를 고민해보는 게 도움이 됨
"""
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)  # 내림차순 정렬

count = 0
for coin in coins:
    if K >= coin:
        count += K // coin
        K %= coin

print(count)
