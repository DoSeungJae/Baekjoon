import sys
input=sys.stdin.readline

N=int(input())

for i in range(N):
    for j in range(i):
        print(" ",end="")
    for j in range(N-i,0,-1):
        print("*",end="")
    for j in range(N-i,1,-1):
        print("*",end="")
    print()
    

