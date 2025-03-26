"""
문제: 프로그래머스 - 문자열이 몇 번 등장하는지 세기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181871

풀이 방법:
- 슬라이싱을 사용해서 비교하여 풀

어려웠던 점:
- range안에 +1을 빼먹는 실수를 함
"""
def solution(myString, pat):
    answer = 0
    np=len(pat)
    for i in range(len(myString)-np+1):
        print(pat, myString[i:i+np])
        if pat == myString[i:i+np]:
            answer+=1
    return answer


"""
좋은 풀이 방법
def solution(myString, pat):
    answer = 0
    for i, x in enumerate(myString) :
        if myString[i:].startswith(pat) :
            answer += 1
    return answer
"""
