"""
사이트: 프로그래머스
문제 이름: [전국 대회 선발 고사](https://school.programmers.co.kr/learn/courses/30/lessons/181851)

풀이 접근 방법:
- 번호와 값을 enumerate를 통해 넣고, 정렬한 후 나온 수식대로 계산하였다.

느낀점:
- 리스트 생성이 많이 익숙해진 거 같다.
"""
def solution(rank, attendance):
    answer = [[rank[i],i] for i,at in enumerate(attendance) if at]
    answer.sort()
    return answer[0][1]*10000+answer[1][1]*100+answer[2][1]
