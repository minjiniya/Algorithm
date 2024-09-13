import sys
input=sys.stdin.readline
S={"STRAWBERRY":0, "BANANA":0, "LIME":0, "PLUM":0}
n=int(input())
for i in range(n):
    a,b=input().split()
    S[a]+=int(b)
for i in S:
    if(S[i]==5):
        print("YES")
        break
    else:
        if(i=="PLUM"):print("NO")