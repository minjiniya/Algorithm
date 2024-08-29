import sys
input=sys.stdin.readline
b=set(chr(i) for i in range(97,123))
while(True):
    a=set(input().rstrip())
    if(' ' in a):a.remove(' ')
    if(a=={'*'}):break
    if(a==b):print("Y")
    else:print("N")