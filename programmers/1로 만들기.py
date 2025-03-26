"""
문제: 프로그래머스 - 1로 만들기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181880

풀이 방법:
- //연산을 활용하여 간략화 시킨후, 1이 아닌 모든 양수는 1로 귀결되므로 while을 사용하였음

어려웠던 점:
- 없음
"""
def solution(num_list):
    answer = 0
    for num in num_list:
        while num!=1:
            num=num//2
            answer+=1
    return answer
