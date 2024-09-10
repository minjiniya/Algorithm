n=int(input())
A={}
for i in range(n):
    a,b=input().split()
    A[b]=a
c=input()
res=''
for i in c:
    res+=A[i]
s,e=map(int,input().split())
print(res[s-1:e])