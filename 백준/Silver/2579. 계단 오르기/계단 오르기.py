import sys
input=sys.stdin.readline
n=int(input())
score=[]
for i in range(n):
    score.append(int(input()))
res=[0]*(n+1)
count=0
for i in range(n+1):
    if(i==0):
        res[i]=0
    elif(i==1):
        res[i]=score[i-1]
    else:
        if(count==0):
            res[i]=max(res[i-1]+score[i-1],res[i-2]+score[i-1])
            if(res[i]==res[i-1]+score[i-1]):
                count+=1
                pre=res[i-2]+score[i-1]
        else:
            res[i]=max(res[i-2]+score[i-1],pre+score[i-1])
            if(res[i]==res[i-2]+score[i-1]):
                count=0
                pre+=score[i-1]
            else:
                pre=res[i-2]+score[i-1]
print(res[n])