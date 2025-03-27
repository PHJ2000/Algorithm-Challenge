"""
사이트: 프로그래머스
문제 이름: [왼쪽 오른쪽](https://school.programmers.co.kr/learn/courses/30/lessons/181890)

풀이 접근 방법:
- l과 r을 찾으면 해당 조건에 맞는 슬라이싱 후 리턴

느낀점:
- range(len(str_list))보다 enumerate가 더 깔끔했다
"""
def solution(str_list):
    if "l" not in str_list and "r" not in str_list:
        return []
    for i, st in enumerate(str_list):
        if st=="l":
            return str_list[:i]
        if st=="r":
            return str_list[i+1:]
