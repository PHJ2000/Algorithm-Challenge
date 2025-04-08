"""
사이트: 백준
문제 이름: [그룹 단어 체커](https://www.acmicpc.net/problem/1316)

풀이 접근 방법:
- 이전 문자와 현재 문자를 비교하여 판별, set 자료구조를 이용

느낀점:
- 파이썬에 in연산자는 정말 최고이다.
"""
def is_group_word(word):
    seen = set()
    prev_char = ''
    for char in word:
        if char != prev_char:
            if char in seen:
                return False
            seen.add(char)
        prev_char = char
    return True

n = int(input())
count = 0
for _ in range(n):
    word = input()
    if is_group_word(word):
        count += 1
print(count)
