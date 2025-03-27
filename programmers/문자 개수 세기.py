"""
사이트: 프로그래머스
문제 이름: [문자 개수 세기](https://school.programmers.co.kr/learn/courses/30/lessons/181902)

풀이 접근 방법:
- 리스트와 ord함수를 이용하여, 구현함

느낀점:
- 처음에 디폴트 딕셔너리를 생각했지만, 리스트로 충분하였고, ord가 떠오르지 않아 고생했다
"""
def solution(my_string):
    s = [0]*52
    for i in my_string:
        if i<='z' and i>='a':
            s[ord(i)-ord('a')+26]+=1
        elif i<='Z' and i>='A':
            s[ord(i)-ord('A')]+=1
        
    return s


"""
좋은 풀이
def solution(my_string):
    answer=[0]*52
    for x in my_string:
        if x.isupper():
            answer[ord(x)-65]+=1
        else:
            answer[ord(x)-71]+=1
    return answer
"""
