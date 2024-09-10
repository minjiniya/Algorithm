a=input()
res=[0]*4
for i in a:
    if(i=="U" or res[0]==1):
        res[0]=1
        if(i=="C" or res[1]==1):
            res[1]=1
            if(i=="P" or res[2]==1):
                res[2]=1
                if(i=="C"):
                    res[3]=1
                    break
    else:continue
if(sum(res)==4):print("I love UCPC")
else:print("I hate UCPC")