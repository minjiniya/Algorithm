import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=set()
b=set()
for i in range(n):
    a.add(input().strip())
for i in range(m):
    b.add(input().strip())
res=a&b
print(len(res))
res=list(res)
res.sort()
for i in res:
    print(i)