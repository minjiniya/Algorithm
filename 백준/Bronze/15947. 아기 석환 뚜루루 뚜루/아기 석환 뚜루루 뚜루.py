n=int(input())
a="baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan".split()
if(n%14 in (3,4,7,8,11,12)):
    res=a[n%14-1]
    for i in range(n//14):res+="ru"
    if(res.count("ru")>=5):print("tu+ru*"+str(res.count("ru")))
    else:print(res)
else:print(a[n%14-1])