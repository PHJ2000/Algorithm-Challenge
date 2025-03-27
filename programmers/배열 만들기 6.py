"""
사이트: 프로그래머스
문제 이름: [배열 만들기 6](https://school.programmers.co.kr/learn/courses/30/lessons/181859)

풀이 접근 방법:
- [-1]인덱싱과 pop을 이용하여 구현했다

느낀점:
- [-1], pop이 필요하다점에서 스택이 생각이 났다.
"""
def solution(arr):
    stk = []
    n=len(arr)
    for i in range(n):
        if not stk:
            stk.append(arr[i])
        elif stk and stk[-1]==arr[i]:
            stk.pop()
        elif stk and stk[-1]!=arr[i]:
            stk.append(arr[i])
    if stk:
        return stk
    else:
        return [-1]
    
    
"""
좋은 풀이
def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])

    return stk or [-1]
"""
