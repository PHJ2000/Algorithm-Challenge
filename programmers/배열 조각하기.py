"""
사이트: 프로그래머스
문제 이름: [배열 조각하기](https://school.programmers.co.kr/learn/courses/30/lessons/181893)

풀이 접근 방법:
- 슬라이스와 enumerate를 활용하여 리스트를 변경항여 해결

느낀점:
- enumerate는 정말 유용하다.
"""
def solution(arr, query):
    for i, ar in enumerate(query):
        if i%2==0:
            arr=arr[:ar+1]
        else:
            arr=arr[ar:]
    return arr
