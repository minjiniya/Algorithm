n,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
count=0
for i in range(n-1,-1,-1):
    count+=k//a[i]
    k%=a[i]
    if(k==0):break
print(count)