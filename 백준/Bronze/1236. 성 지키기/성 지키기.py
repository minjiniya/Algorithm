import sys
input=sys.stdin.readline
n,m=map(int,input().split())
row=[1 for i in range(n)]
col=[1 for i in range(m)]
res=0
for i in range(n):
    a=input()
    if("X" in a):row[i]=0
    for j in range(m):
        if(a[j]=="X"):
            col[j]=0
print(max(sum(row),sum(col)))