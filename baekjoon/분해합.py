"""
사이트: 백준
문제 이름: [분해합](https://www.acmicpc.net/problem/2231)

풀이 접근 방법:
- 본인과 자릿수의 합으로 N을 만들 수 있는 최소 값을 찾는 문제다. 일단 다 한다고 가정했을 떄, 크기에 따라서
- 범위를 제한 할 수 있다. 2자리수 최대는 99+18=117, 3자리수는 999+27=1026 아니지, 어떻게 제한 못하나?
- N이 3자리라면, 27아래 부터 시작하면 되겠지? 그래야 맞으니깐 말이야. 그러니깐 자릿수 *9부터 시작해서 N까지 보면 되는 것
- 그렇다면, 시간도 굉장히 적게 걸려서 다 보면 된다는 결론이 된다.

느낀점:
- for else문법이 있다는 것을 처음 알았다. 놀랍다. 자릿수 합을 sum(map(int,str(i)))로 축약하다는 것이 놀랍다.
- 
"""
N = int(input())
ja = N-len(str(N))*9
if ja<0:
    ja=len(str(N))*1
for i in range(ja,N+1):
    if i==N:
        print(0)
        break
    s=i
    for j in str(i):
       s+=int(j)
       if s>N:
           break
    if N==s:
        print(i)
        break
"""
좋은 풀이
N = int(input())

# 생성자의 최소 시작값은 N - 9 * 자릿수
start = max(0, N - 9 * len(str(N)))

for i in range(start, N):
    digit_sum = i + sum(map(int, str(i)))  # 각 자리수 더함
    if digit_sum == N:
        print(i)
        break
else:
    print(0)
"""
