"""
사이트: 프로그래머스
문제 이름: [x만큼 간격이 있는 n개의 숫자](https://school.programmers.co.kr/learn/courses/30/lessons/12954)

풀이 접근 방법:
- 리스트 컴프리헨션을 이용해서 풀었다.

느낀점:
- 처음에는 range(x,x*n,n)으로 진행했으나, 1,n+1이 더 편리하다느 것을 알았다.
"""
def solution(x, n):
    return [i*x for i in range(1,n+1)]
