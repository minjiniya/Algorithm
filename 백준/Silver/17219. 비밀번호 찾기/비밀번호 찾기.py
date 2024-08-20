import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a={}
for i in range(n):
    s,p=input().split()
    a[s]=p
for i in range(m):
    s=input().strip()
    print(a[s])