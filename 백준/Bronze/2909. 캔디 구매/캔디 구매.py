c,k=map(int,input().split())
if(c%(10**k)<(10**k)/2):c=(c//(10**k))*(10**k)
else:c=(c//(10**k)+1)*(10**k)
print(c)