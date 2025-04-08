"""
사이트: 백준
문제 이름: [다이얼](https://www.acmicpc.net/problem/5622)

풀이 접근 방법:
- if문을 활용하여 해결

느낀점:
- 딕셔너리 formkeys와 **딕셔너리 언패킹 연산을 알게되어 좋았다
"""
s=input()
a=0
for c in s:
    if c in "ABC":
        a+=3
    elif c in "DEF":
        a+=4
    elif c in "GHI":
        a+=5
    elif c in "JKL":
        a+=6
    elif c in "MNO":
        a+=7
    elif c in "PQRS":
        a+=8
    elif c in "TUV":
        a+=9
    elif c in "WXYZ":
        a+=10
print(a)
"""
좋은 풀이
s = input()
dial_map = {
    **dict.fromkeys("ABC", 3),
    **dict.fromkeys("DEF", 4),
    **dict.fromkeys("GHI", 5),
    **dict.fromkeys("JKL", 6),
    **dict.fromkeys("MNO", 7),
    **dict.fromkeys("PQRS", 8),
    **dict.fromkeys("TUV", 9),
    **dict.fromkeys("WXYZ", 10),
}

total_time = sum(dial_map[c] for c in s)
print(total_time)

s = input()
dial = [3, 3, 3,   # ABC
        4, 4, 4,   # DEF
        5, 5, 5,   # GHI
        6, 6, 6,   # JKL
        7, 7, 7,   # MNO
        8, 8, 8, 8,  # PQRS
        9, 9, 9,   # TUV
        10,10,10,10]  # WXYZ

total_time = 0
for c in s:
    idx = ord(c) - ord('A')  # A:0, B:1, ..., Z:25
    total_time += dial[idx]

print(total_time)
"""
