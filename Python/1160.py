import sys
input=sys.stdin.readline
LEN=2

m,a,c,x0,n,g=map(int,input().split())
a%=m
c%=m
x0%=m

seq=[[a,0],[c,1]]
seq2=[[x0,1],[0,0]]

def matrixMultiple(a:list,b:list)->list:
    res=[[0 for _ in range(LEN)] for _ in range(LEN)]

    for i in range(LEN):
        for j in range(LEN):
            for k in range(LEN):
                res[i][j]+=(a[i][k]*b[k][j])


    return [[x%m for x in row] for row in res]

def matrixPower(a:list,b:int)->list:
    if(b==1):
        return [[x%m for x in row] for row in a]
    elif(b%2==0):
        temp=matrixPower(a,b//2)
        return [[x%m for x in row] for row in matrixMultiple(temp,temp)]
    else:
        temp=matrixPower(a,b//2)
        return [[x%m for x in row] for row in matrixMultiple(a,matrixMultiple(temp,temp))]
    

resSeq=matrixPower(seq,n)
print(((x0*resSeq[0][0]+resSeq[1][0])%m)%g)



