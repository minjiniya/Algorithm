n,k=map(int,input().split())
a=list(map(int,input().split()))
res=[]
for i in range(k-1,n):
    ans=0
    for j in range(k):
        ans+=a[i-j]
    res.append(ans)
print(max(res))