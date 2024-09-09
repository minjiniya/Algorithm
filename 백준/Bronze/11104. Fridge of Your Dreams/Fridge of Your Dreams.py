import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    a=int(input())
    print(int("0b"+str(a),2))