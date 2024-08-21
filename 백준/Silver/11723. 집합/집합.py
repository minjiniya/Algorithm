import sys
input=sys.stdin.readline
m=int(input())
S=set()
for i in range(m):
    a=input().split()
    if(a[0]=="all"):
        S={i for i in range(1,21)}
    elif(a[0]=="empty"):
        S.clear()
    else:
        x=int(a[1])
        if(a[0]=="add"):S.add(x)
        elif(a[0]=="remove"):
            if(x in S):S.remove(x)
            else:continue
        elif(a[0]=="check"):
            if(x in S):print(1)
            else:print(0)
        elif(a[0]=="toggle"):
            if(x in S):S.remove(x)
            else:S.add(x)