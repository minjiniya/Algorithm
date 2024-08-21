def d(n):
    if(n==1):
        a[n]=0
        return a[n]
    else:
        if(a[n]!=0):return a[n]
        if(n%3==0 and n%2==0):
            a[n]=min(d(n//3)+1,d(n//2)+1)
        elif(n%3==0):
            a[n]=min(d(n//3)+1,d(n-1)+1)
        elif(n%2==0):
            a[n]=min(d(n//2)+1,d(n-1)+1)
        else:
            a[n]=d(n-1)+1
        return a[n]
n=int(input())
a=[0]*(n+1)
print(d(n))