import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    a,b=input().split()
    a=list(a)
    a.reverse()
    a="".join(a)
    b=list(b)
    b.reverse()
    b="".join(b)
    res=list(str(int(a)+int(b)))
    res.reverse()
    print(int("".join(res)))