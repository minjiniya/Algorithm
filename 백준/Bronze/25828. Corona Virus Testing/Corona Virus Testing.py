g,p,t=map(int,input().split())
i=g+p*t
if(i>g*p):print(1)
elif(i<g*p):print(2)
else:print(0)