import sys
import heapq
input=sys.stdin.readline
n=int(input())
a=[]
for i in range(n):
    x=int(input())
    if(x==0):
        if(len(a)==0):
            print(0)
        else:
            b=heapq.heappop(a)
            print(b)
    else:heapq.heappush(a,x)