"""
사이트: 프로그래머스
문제 이름: [자연수 뒤집어 배열로 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12932)

풀이 접근 방법:
- 리스트 컴프리헨션과 reversed를 활용하여 구현

느낀점:
- 리스트 컴프리헨션이 정말 편리하다, map은 생각을 못 했다.
"""
def solution(n):
    answer = [int(i) for i in reversed(str(n))]
    return answer


"""
좋은 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
"""
