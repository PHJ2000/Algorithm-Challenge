"""
사이트: 백준
문제 이름: [과제 안 내신 분..?](https://www.acmicpc.net/submit/5597)

풀이 접근 방법:
- 리스트를 활용해서 2번 접근하여 구현

느낀점:
- 31로 한 개 초과해서 만든 후 출력하는게 좀 더 가독성이 좋아보인다.
"""
l=[0]*31
for i in range(28):
    c=int(input())
    l[c]=1
for i in range(1,31):
    if l[i]==0:
        print(i)
"""
좋은 풀이
submitted = {int(input()) for _ in range(28)}
for student in sorted(set(range(1, 31)) - submitted):
    print(student)
"""
