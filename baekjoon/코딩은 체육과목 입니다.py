"""
사이트: 백준
문제 이름: [코딩은 체육과목 입니다](https://www.acmicpc.net/submit/25314)

풀이 접근 방법:
- 간단한 입출력 문제다

느낀점:
- 문제가 너무 재밌다. 오랜만에 end=" "을 쓴다.
"""
n=int(input())
for i in range(n//4):
    print("long",end=" ")
print("int")
