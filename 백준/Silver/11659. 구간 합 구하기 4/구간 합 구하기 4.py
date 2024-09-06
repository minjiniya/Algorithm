import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))
res=[0]
for i in a:
    res.append(res[-1]+i)
for k in range(m):
    i,j=map(int,input().split())
    print(res[j]-res[i-1])