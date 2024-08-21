import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a={}
for i in range(n):
    s=input().strip()
    a[s]=i+1
b = {v:k for k,v in a.items()}
for i in range(m):
    l=input().strip()
    if(l in a):print(a[l])
    else:print(b[int(l)])