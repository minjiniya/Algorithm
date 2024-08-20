n=int(input())
p=list(map(int,input().split()))
p.sort()
res=0
for i in range(n):
    time=0
    for j in range(i+1):
        time+=p[j]
    res+=time
print(res)