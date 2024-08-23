n = int(input())
a=[]
res = 0
for i in range(1,n+1):
    if(n%i==0):
        a.append(i)
print(sum(a)*5-24)