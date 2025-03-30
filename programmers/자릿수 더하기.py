"""
사이트: 프로그래머스
문제 이름: [자릿수 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/12931)

풀이 접근 방법:
- 제너레이터 표현식을 활용하여 한줄로 구현
- 문자열로 만든 후 for문으로 순회

느낀점:
- 처음에 리스트 컴프리핸션으로 해결하려고 하였으나, 굳이 그럴 필요가 없음을 느꼈다. 이 형식을 자주 사용할만 하다.
"""
def solution(n):
    return sum(int(i) for i in str(n))
