import sys
input=sys.stdin.readline

a=input().strip()
b=input().strip()

dp=[[0]*(len(a)+1) for _ in range(len(b)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if(a[i-1]==b[j-1]):
            dp[j][i]=dp[j-1][i-1]+1
        else:
            dp[j][i]=max(dp[j-1][i],dp[j][i-1])

print(dp[-1][-1])
