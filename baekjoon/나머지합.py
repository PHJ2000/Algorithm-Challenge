import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = 0
remainder_count = [0] * m
remainder_count[0] = 1
answer = 0
for num in arr:
    prefix_sum += num
    r = prefix_sum % m
    answer += remainder_count[r]
    remainder_count[r] += 1
    
print(answer)
