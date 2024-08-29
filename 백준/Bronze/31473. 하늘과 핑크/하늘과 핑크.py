n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
j=2
k=1
A,B=sum(a),sum(b)
for i in range(100000):
    if(A==1 or B==1):break
    if(A%j==0 and B%j==0):
        k*=j
        A=int(A/j)
        B=int(B/j)
    else:j+=1
print(int(sum(b)/k),int(sum(a)/k))