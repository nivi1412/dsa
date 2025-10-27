# DP_GuessnumHighLow_bottomup.py

import math

n=int(input("enter the number count: "))
p,q=1,n 

dp=[[-1 for _ in range(n+1)]for _ in range(n+1)]

for i in range(n+1):
	for j in range(n+1):
		if j<=i:
			dp[i][j]=0
		if j==i+1:
			dp[i][j]=min(i,j)


for i in range(n,0,-1):
	for j in range(n,i,-1):
		res=math.inf
		for k in range(i,j):
			val=k+max(dp[i][k-1],dp[k+1][j])
		res=min(res,val)
print(dp)	
