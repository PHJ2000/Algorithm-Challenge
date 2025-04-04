"""
사이트: 백준
문제 이름: [알파벳 찾기](https://www.acmicpc.net/submit/10809)

풀이 접근 방법:
- chr을 이용하여 유니코드를 문자로 변환하고 index로 구현

느낀점:
- chr이 아니라 str로 하려고 했으나, 작동원리가 다르다는 걸 알게 되었다.
"""
s = input()
for i in range(26):
    ch = chr(i + ord('a'))  # 'a'부터 'z'까지 알파벳 문자 생성
    if ch in s:
        print(s.index(ch), end=" ")
    else:
        print(-1, end=" ")
