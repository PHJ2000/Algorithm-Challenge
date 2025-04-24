"""
사이트: 백준
문제 이름: [나무 자르기](https://www.acmicpc.net/problem/2805)

풀이 접근 방법:
- 이분 탐색(Parametric Search) 활용
- 절단기 높이를 이분 탐색하여 적어도 M미터의 나무를 얻을 수 있는 최대 높이를 찾음
- 각 중간 높이(mid)마다 잘린 나무의 길이 합을 계산하여 조건을 만족하는지 확인

느낀점:
- 이분 탐색을 응용하여 최적의 값을 찾는 방법을 익힐 수 있는 좋은 문제
- 탐색 범위 설정과 조건 확인의 중요성을 체감함
"""
import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    trees = list(map(int, sys.stdin.readline().split()))

    low, high = 0, max(trees)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        total = sum((tree - mid) for tree in trees if tree > mid)

        if total >= M:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    print(result)

if __name__ == "__main__":
    main()
