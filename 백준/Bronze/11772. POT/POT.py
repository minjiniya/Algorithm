t=int(input())
res=0
for i in range(2,2+t):
    a=input()
    res+=int(a[:-1])**int(a[-1])
print(res)