def res(n):
    if(n==0):
        a[0]=[1,0]
        return a[n]
    elif(n==1):
        a[1]=[0,1]
        return a[n]
    elif(a[n]!=[0,0]):return a[n]
    else:
        a[n]=[res(n-1)[0]+res(n-2)[0],res(n-1)[1]+res(n-2)[1]]
        return a[n]
t=int(input())
for i in range(t):
    n=int(input())
    a=[[0,0] for i in range(n+1)]
    x=res(n)
    print(x[0],x[1])