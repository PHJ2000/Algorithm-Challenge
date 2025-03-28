"""
사이트: 프로그래머스
문제 이름: [무작위로 K개의 수 뽑기](https://school.programmers.co.kr/learn/courses/30/lessons/181858)

풀이 접근 방법:
- set을 사용하여 구현을 진행하였다.

느낀점:
- list(set())를 사용했을 때 정답인 줄 알았지만, 순서가 지정되지 않기 때문에 틀렸다는 것을 알게되었다.
"""

def solution(arr, k):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
            if len(result) == k:
                break

    # 부족한 길이만큼 -1 채우기
    while len(result) < k:
        result.append(-1)

    return result
