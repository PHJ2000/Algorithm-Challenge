"""
사이트: 백준  
문제 이름: [칸토어 집합](https://www.acmicpc.net/problem/4779)

풀이 접근 방법:  
- 재귀적으로 문자열을 구성  
- 길이 3^n의 문자열에서 가운데 1/3을 공백으로 바꾸고, 나머지 부분에 대해 같은 작업을 반복  
- 전체 문자열을 리스트로 만들고, 필요한 위치에 공백을 삽입

느낀점:  
- 재귀 호출이 문자열이나 구간에 어떻게 적용되는지 감이 잡혔음  
- 시각적으로 재귀의 결과를 그려보며 문제 해결 능력이 향상됨  
"""
def cantor(start, end, arr):
    if end - start < 3:
        return
    third = (end - start) // 3
    for i in range(start + third, start + 2 * third):
        arr[i] = ' '
    cantor(start, start + third, arr)
    cantor(start + 2 * third, end, arr)

while True:
    try:
        N = int(input())
        length = 3 ** N
        arr = ['-'] * length
        cantor(0, length, arr)
        print(''.join(arr))
    except EOFError:
        break
