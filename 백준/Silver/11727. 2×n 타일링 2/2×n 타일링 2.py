n=int(input())
a=[]
for i in range(n):
    if(i==0):a.append(1)
    elif(i==1):a.append(3)
    else:
        a.append(a[i-2]*2+a[i-1])
print(a[-1]%10007)