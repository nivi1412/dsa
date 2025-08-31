#DP_Triangle.py

import ast
triangle=input("enter the triangle list")
triangle=ast.literal_eval(triangle)

dp=[[0]*(i+1) for i in range(len(triangle))]

for i in range(len(dp)):
	dp[len(dp)-1][i]=triangle[len(dp)-1][i]

for i in range(len(dp)-2,-1,-1):
	for j in range(len(dp[i])):
		dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]

print(dp)
print(dp[0][0])

