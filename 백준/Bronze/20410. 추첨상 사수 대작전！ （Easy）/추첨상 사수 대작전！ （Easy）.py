m,s,x1,x2=map(int,input().split())
b=0
for i in range(m):
    for j in range(m):
        if(x1==(i*s+j)%m):
            if(x2==(i*x1+j)%m):
                print(i,j)
                b = 1
                break
            else:continue
        else:continue
    if(b==1):break