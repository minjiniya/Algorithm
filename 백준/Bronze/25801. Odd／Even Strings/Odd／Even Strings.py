a=input()
b=set(a)
res=set()
for i in b:
    if(a.count(i)%2==0):res.add(0)
    else:res.add(1)
if(res=={0}):print(0)
elif(res=={1}):print(1)
else:print("0/1")