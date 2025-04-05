"""
사이트: 프로그래머스
문제 이름: [제일 작은 수 제거하기](https://school.programmers.co.kr/learn/courses/30/lessons/12935)

풀이 접근 방법:
- sorted와 인덱스를 이용해서 해결

느낀점:
- sorted가 리스트를 리턴하기에 인덱스를 쓰니 좋았다.
"""
def solution(arr):
    if len(arr)==1:
        return [-1]
    arr.remove(min(arr))
    return arr
