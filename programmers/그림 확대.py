"""
사이트: 프로그래머스
문제 이름: [그림 확대](https://school.programmers.co.kr/learn/courses/30/lessons/181836)

풀이 접근 방법:
- k배가 가로 세로 모두 적용이 되므로 한 픽셀을 k*k로 만들면 됩니다. 이걸 어떻게 적용시킬 것인가는 반복문을 활용
- .join을 활용하여서 문자열을 모은 후 집어넣기, 세로에 경우에는 단순 반복으로 해결

느낀점:
- 문제 풀이 중 배운 점이나 어려웠던 점
"""
def solution(picture, k):
    result = []
    for row in picture:
        # 각 문자를 k번 반복하여 가로 방향 확장
        scaled_row = ''.join([char * k for char in row])
        # 만들어진 row를 세로로 k번 반복하여 전체 이미지 확장
        for _ in range(k):
            result.append(scaled_row)
    return result
