import sys
input=sys.stdin.readline
n=int(input())
x=int(input())
c=[]
for i in range(x):
    v=list(map(int,input().split()))
    if(i==0):
        c.append(v)
        continue
    for pair in c:
        if(v[0] in pair):
            if(v[1] in pair):pass
            else:pair.append(v[1])
        elif(v[1] in pair):
            pair.append(v[0])
        else:
            if(pair==c[-1]):
                c.append(v)
                break
for i in range(1,len(c)):
    for j in range(i):
        set_a=set(c[j])
        set_b=set(c[i])
        if(set_a&set_b!=set()):
            c[i]=list(set_a|set_b)
            c[j]=[]
for row in c:
    if(1 in row):
        res=len(row)
        break
if(n==1):res=1
print(res-1)