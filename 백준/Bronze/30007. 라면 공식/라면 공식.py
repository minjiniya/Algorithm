import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    a,b,x=map(int,input().split())
    print(a*(x-1)+b)