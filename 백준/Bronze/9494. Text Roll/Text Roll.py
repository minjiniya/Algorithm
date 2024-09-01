import sys
input=sys.stdin.readline
while(True):
    n=int(input())
    if(n==0):break
    b=0
    for i in range(n):
        a=input()
        for j in range(b,len(a)):
            if(j==0):continue
            if(a[j-1]!=" " and a[j]==" "):
                b=j
                break
            else:b=len(a)-1
    print(b+1)