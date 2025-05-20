import sys
input=sys.stdin.readline
n,m=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]
B=[list(map(int,input().split())) for _ in range(n)]
C=[[A[i][j]+B[i][j] for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(C[i][j],end=" ")
    print()
