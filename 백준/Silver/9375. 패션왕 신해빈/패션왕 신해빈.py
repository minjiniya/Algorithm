import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    c={}
    n=int(input())
    for j in range(n):
        a,b=input().split()
        if(b in c):c[b]+=1
        else:c[b]=1
    total=1
    for item in c:
        total*=c[item]+1
    print(total-1)