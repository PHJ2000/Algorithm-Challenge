"""
사이트: 프로그래머스
문제 이름: [정사각형으로 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/181830)

풀이 접근 방법:
- 행과 열에 길이를 구한 후 문제에서 설명한대로 구현하면 된다.

느낀점:
- if문을 쓰지않고, range에 n-m, m-n으로 하는 방법이 더 깔금하다.
"""
def solution(arr):
    r=len(arr)
    c=len(arr[0])
    if r==c:
        return  arr
    if r>c:
        for i in range(r):
            for j in range(r):
                if j>=c:
                    arr[i].append(0)
        return arr
    else:
        for i in range(c):
            if i>=r:
                arr.append([0]*c)
        return arr
"""
깔끔한 풀이
def solution(arr):
    n=len(arr)
    m=len(arr[0])
    if n>m:
        for i in range(n):
            for j in range(n-m):
                arr[i].append(0)
    else:
        for i in range(m-n):
            arr.append([0]*m)

    return arr
"""
