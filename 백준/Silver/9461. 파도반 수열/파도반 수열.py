import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    a=[1,1,1,2,2]
    n=int(input())
    if(n<=5):print(a[n-1])
    else:
        for i in range(5,n):
            a.append(a[i-1]+a[i-5])
        print(a[-1])