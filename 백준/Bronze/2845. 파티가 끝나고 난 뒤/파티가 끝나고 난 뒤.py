l,p=map(int,input().split())
a=list(map(int,input().split()))
for i in range(len(a)):
    a[i]-=l*p
for i in a:
    print(i,end=" ")