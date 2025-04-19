"""
사이트: 백준
문제 이름: [큐 2](https://www.acmicpc.net/problem/18258)

풀이 접근 방법:
- 명령 개수 N이 최대 2,000,000이므로 각 연산을 모두 O(1)에 처리해야 함
- collections.deque를 사용해 append, popleft 연산을 상수 시간에 수행
- back 명령에서도 O(1)로 결과를 내기 위해 push 시 마지막 값을 back_val 변수에 저장
- 출력 횟수를 최소화하기 위해 결과를 리스트에 모아 한 번에 sys.stdout.write로 출력

느낀점:
- 파이썬에서도 적절한 자료구조(deque)와 빠른 입출력(sys.stdin.readline, sys.stdout.write)을 활용하면
  대용량 시뮬레이션 문제를 충분히 해결할 수 있음을 경험함
- back 연산을 deque[-1]로도 처리할 수 있지만, 별도의 변수를 두어 의도를 명확히 하는 방법도 유용함
- 문제 수준은 실버 4지만, IO 최적화와 메모리 접근 방식을 고려하는 연습에 도움이 되었음
"""
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n = int(input())
    q = deque()
    back_val = None       # 마지막에 push된 값을 저장
    output = []

    for _ in range(n):
        cmd = input().split()
        op = cmd[0]

        if op == 'push':
            q.append(cmd[1])
            back_val = cmd[1]
        elif op == 'pop':
            output.append(q.popleft() if q else '-1')
        elif op == 'size':
            output.append(str(len(q)))
        elif op == 'empty':
            output.append('0' if q else '1')
        elif op == 'front':
            output.append(q[0] if q else '-1')
        elif op == 'back':
            output.append(back_val if q else '-1')

    # 한 번에 출력
    sys.stdout.write('\n'.join(output))


if __name__ == '__main__':
    main()
