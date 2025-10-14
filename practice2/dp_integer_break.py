# dp_integer_break.py
import math

n=int(input("enter the n value:"))

dp=[-math.inf]*(n+1)

dp[0]=0
dp[1]=1
dp[2]=2
dp[3]=2


for num in range(3,n+1):
	for i in range(1,num):
		dp[num]=max(dp[num],i*(num-i),i*dp[num-i])

print(dp)
