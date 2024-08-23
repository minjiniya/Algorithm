import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    count=0
    n=int(input())
    a=[]
    for i in range(n):
        if(i==0):a.append(1)
        elif(i==1):a.append(2)
        elif(i==2):a.append(4)
        else:a.append(a[i-3]+a[i-2]+a[i-1])
    print(a[n-1])