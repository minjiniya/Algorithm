import sys
input=sys.stdin.readline
def GCD(a,b):
    a,b=max(a,b),min(a,b)
    while(b!=0):
        c=a-b*(a//b)
        a=b
        b=c
    return a
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    x=GCD(a,b)
    print(int(a*b/x))