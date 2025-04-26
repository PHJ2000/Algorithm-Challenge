"""
사이트: 백준
문제 이름: [곱셈](https://www.acmicpc.net/problem/1629)

풀이 접근 방법:
- 분할정복을 통해서 수 폭발을 막는다.
- 거듭제곱을 절반식 나누는 방식으로 해결
느낀점:
- 처음에 재귀를 생각하지 못했다. mod연산에서 //2로 나누는 방식이 새롭다
"""
def pow_mod(A, B, C):
    if B == 0:
        return 1
    elif B == 1:
        return A % C
    half = pow_mod(A, B // 2, C)
    if B % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * A) % C

A, B, C = map(int, input().split())
print(pow_mod(A, B, C))
