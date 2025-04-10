"""
사이트: 백준
문제 이름: [알고리즘 수업 - 알고리즘의 수행 시간 6](https://www.acmicpc.net/problem/24257)

풀이 접근 방법:
- 처음에 일일이 반복문으로 점화식 찾으려고 노력하였다.
- 못 찾았기에, gpt에 도움으로 1<=i<j<k<=N인 3수의 조합을 구하는 문제인 것을 알게되었다.
- 공식을 적용하여 해결

느낀점:
- 반복문이 었기에, 세 반복문을 개별로 값을 추산하고 더하는 방식으로 식을 만들어 볼려고 하였으나
- 실패하였다. 정말 조합 인지는 생각도 하지 못했다. 관점이 바뀌게 되었다.
"""
def count_triplet_loops(n):
    count = n * (n - 1) * (n - 2) // 6
    degree = 3  # 최고차항의 차수
    return count, degree

n = int(input())
count, degree = count_triplet_loops(n)
print(count)
print(degree)
