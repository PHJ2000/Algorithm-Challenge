"""
사이트: 프로그래머스
문제 이름: [정수 내림차순으로 배치하기](https://school.programmers.co.kr/learn/courses/30/lessons/12933)

풀이 접근 방법:
- 문자열로 만든 후, sorted를 이용하고, 그 후 join으로 합친 후 정수형으로 변환하고 구현
- 내림차순이기 때문에, 정수로 변환시 0이 지워지는 문제도 자유로움

느낀점:
- reverse와 reversed가 헷갈려 고생을 하였다.
"""
def solution(n):
    return int("".join(sorted(str(n),reverse=True)))
