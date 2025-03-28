"""
사이트: 프로그래머스
문제 이름: [문자열 여러 뒤집기](https://school.programmers.co.kr/learn/courses/30/lessons/181913)

풀이 접근 방법:
- 슬라이싱을 이용해서 접근
- 슬라이싱 후 합쳐서 진행함

느낀점:
- reversed가 기억이 나지 않아. 어려웠다. [s:e+1][::-1] 형식 정말 좋은 거 같다.
- 나도 다음에 리스트 변환후 진행해야겠다.
"""
def solution(my_string, queries):
    for s,e in queries:
        first=my_string[0:s]
        second=my_string[e+1:]
        re=''.join(reversed(my_string[s:e+1]))
        my_string=first+re+second
    return my_string
"""
좋은 풀이
def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)
"""
