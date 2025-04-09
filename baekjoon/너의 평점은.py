"""
사이트: 백준
문제 이름: [너의 평점은](https://www.acmicpc.net/problem/25206)

풀이 접근 방법:
- 딕셔너리를 이용해서 구현함

느낀점:
- 실수의 자릿수 제한을 하는 법을 까먹어 곤혹스러웠다.
"""
a=0
hs=0
d={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0}
for i in range(20):
    s, h, r = input().split()
    h=float(h)
    if r!="P":
        a+=h*d[r]
        hs+=h
print("{:4f}".format(a/hs))
