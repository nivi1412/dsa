#DP11_MinCostClimbingStairs.py
import ast

cost=input("enter the array of cost: ")
cost=ast.literal_eval(cost)

dp=[0]*len(cost)

dp[0]=0
dp[1]=0
count=0

for i in range(2,len(cost),+1):
	dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])

print(dp)
print(dp[-1]+cost[-1])
