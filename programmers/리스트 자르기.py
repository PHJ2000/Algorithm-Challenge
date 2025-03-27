"""
사이트: 프로그래머스
문제 이름: [리스트 자르기](https://school.programmers.co.kr/learn/courses/30/lessons/181897)

풀이 접근 방법:
- 간단한 조건 분기와 리스트 슬라이스를 이용하여 품

느낀점:
- 처음에 리스트를 언팩(*)할려고 하였으나 리스트는 그런 과정이 필요없다는 것을 느꼈다.
  리스트 슬라이스에서 [::c] c에 해당하는 부분이 굉장히 유용했다
"""
def solution(n, slicer, num_list):
    a,b,c=slicer
    if n==1:
        return num_list[0:b+1]
    if n==2:
        return num_list[a:]
    if n==3:
        return num_list[a:b+1]
    if n==4:
        return num_list[a:b+1:c]
