"""
사이트: 프로그래머스
문제 이름: [나누어 떨어지는 숫자 배열](https://school.programmers.co.kr/learn/courses/30/lessons/12910)

풀이 접근 방법:
- 리스트 컴프리헨션과 정렬을 이용하여 풀었다.

느낀점:
- or [-1]과 같이 or연산자의 특성을 이용한 방식이 신선했다.
"""
def solution(arr, divisor):
    answer = [i for i in arr if i%divisor==0]
    if answer:
        return sorted(answer)
    return [-1]


"""
좋은 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
"""
