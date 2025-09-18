# DP_Perfect_Squares.py
#bottom up
import math

n=int(input("enter the num: "))
dp={}
for i in range(1,4):
	dp[i]=i
for i in range(4,n+1,+1):
	j=math.isqrt(i)
	rem=i-(j*j)
	if rem==0:
		dp[i]=1
	else:
		dp[i]=1+dp[rem]
print(dp[n])










