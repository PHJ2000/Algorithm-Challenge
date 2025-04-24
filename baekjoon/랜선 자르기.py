"""
사이트: 백준
문제 이름: [랜선 자르기](https://www.acmicpc.net/problem/1654)

풀이 접근 방법:
- 이분 탐색(Binary Search) 활용
- 가능한 랜선의 최대 길이를 찾기 위해 이분 탐색 수행
- 각 중간 길이(mid)마다 잘라진 랜선의 개수를 계산하여 조건을 만족하는지 확인
- 조건을 만족하면 더 긴 길이를 탐색하고, 만족하지 않으면 더 짧은 길이를 탐색

느낀점:
- 이분 탐색을 응용하여 최적의 값을 찾는 방법을 익힐 수 있는 좋은 문제
- 탐색 범위 설정과 조건 확인의 중요성을 체감함
"""
import sys

def count_cables(cables, length):
    return sum(cable // length for cable in cables)

def main():
    K, N = map(int, sys.stdin.readline().split())
    cables = [int(sys.stdin.readline()) for _ in range(K)]

    low, high = 1, max(cables)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if count_cables(cables, mid) >= N:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    print(result)

if __name__ == "__main__":
    main()
