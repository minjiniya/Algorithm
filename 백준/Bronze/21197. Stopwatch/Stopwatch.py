import sys
input=sys.stdin.readline
n=int(input())
if(n%2==1):print("still running")
else:
    res=0
    for i in range(n):
        if(i%2==0):
            a=int(input())
            continue
        else:
            b=int(input())
            res+=b-a
    print(res)