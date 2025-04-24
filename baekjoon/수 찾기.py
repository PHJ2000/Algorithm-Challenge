"""
사이트: 백준
문제 이름: [수 찾기](https://www.acmicpc.net/problem/1920)

풀이 접근 방법:
- 이진 탐색(Binary Search) 활용
- 주어진 수열을 정렬한 후, 각 찾고자 하는 수에 대해 이진 탐색 수행
- 시간 복잡도: O(N log N + M log N)

느낀점:
- 이진 탐색의 개념과 구현 방법을 익힐 수 있는 좋은 문제
- 정렬된 배열에서의 탐색 효율성을 체감함
"""
import sys
input = sys.stdin.read

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

# 입력 받기
data = input().split()
n = int(data[0])
A = list(map(int, data[1:n+1]))
m = int(data[n+1])
M = list(map(int, data[n+2:]))

# 정렬
A.sort()

# 각 원소에 대해 이진 탐색 수행
results = [binary_search(A, num) for num in M]

# 결과 출력
for res in results:
    print(res)

