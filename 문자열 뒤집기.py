"""
문제: 프로그래머스 - 문자열 뒤집기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181905

풀이 방법:
- reversed를 join으로 묶은 다음 앞에 부분과 뒤에 부분을 더해주었다.

어려웠던 점:
- reversed가 리스트 형태로 리턴해주어서 .join으로 묶어야 했다.
"""

def solution(my_string, s, e):
    return my_string[0:s]+''.join(reversed(my_string[s:e+1]))+my_string[e+1:]

"""
def solution(my_string, s, e):
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]
    
조금 더 깔끔한 코드
"""
