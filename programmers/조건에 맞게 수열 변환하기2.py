"""
사이트: 프로그래머스
문제 이름: [조건에 맞게 수열 변환하기2](https://school.programmers.co.kr/learn/courses/30/lessons/181881)

풀이 접근 방법:
- deepcopy를 이용해서 간단하게, 반복되는 지를 체크하여 품

느낀점:
- 처음에 얕은 복사를 하였다가, 잘못됨을 느끼고 깊은 복사를 진행하였다.
"""
from copy import deepcopy
def solution(arr):
    answer = 0
    prev=[]
    while prev!=arr:
        prev=deepcopy(arr)
        for i, a in enumerate(arr):
            if a>=50 and a%2==0:
                arr[i]=arr[i]/2
            if a<50 and a%2==1:
                arr[i]=arr[i]*2+1
#        print(prev, arr)
        if prev!=arr:
            answer+=1
    return answer
