# DP_GuessnumHighLow.py
import math

def GuessnumHighLow(i,j,dp):
	res=math.inf
	if j<=i:
		return 0
	if j==i+1:
		return min(i,j)
	if dp[i][j]!=-1:
		return dp[i][j]

	for k in range(i,j+1):
		val=k+max(GuessnumHighLow(i,k-1,dp),GuessnumHighLow(k+1,j,dp))
		res=min(res,val)

	dp[i][j]=res
	return dp[i][j]


n=int(input("enter the number count: "))
i=1
j=n

dp=[[-1 for _ in range(n+1)] for _ in range(n+1)]
dp[0][0]=0

ans=GuessnumHighLow(i,j,dp)

print(dp)
print("Ans:",ans)