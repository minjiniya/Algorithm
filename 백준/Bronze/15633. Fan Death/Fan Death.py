n = int(input())
res = 0
for i in range(1,n+1):
    if(n%i==0):
        res+=i
print(res*5-24)