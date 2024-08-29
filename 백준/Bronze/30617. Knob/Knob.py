import sys
input=sys.stdin.readline
T=int(input())
res=0
for i in range(T):
    l,r=map(int,input().split())
    if(l==r and l!=0):res+=1
    if(i==0):
        pl,pr=l,r
        continue
    if(pl==l and l!=0):res+=1
    if(pr==r and r!=0):res+=1
    pl,pr=l,r
print(res)