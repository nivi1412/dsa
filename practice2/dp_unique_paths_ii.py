# DP_Unique_pathsII.py
import ast

obstacle_grid=input("enter the obstacle_grid: ")
obstacle_grid=ast.literal_eval(obstacle_grid)
obstacle_row=False
obstacle_col=False
dp=obstacle_grid

for i in range(1,len(dp)):
	if not (dp[i][0]) and not(obstacle_row):
		dp[i][0]=1
	else:
		dp[i][0]=0
		obstacle_row=True
for j in range(len(dp[0])):
	if not (dp[0][j]) and not(obstacle_col):
		dp[0][j]=1
	else:
		dp[0][j]=0
		obstacle_col=True
dp[0][0]=0
for i in range(1,len(dp)):
	for j in range(1,len(dp[0])):
		if not dp[i][j]:
			dp[i][j]=dp[i-1][j]+dp[i][j-1]
		else:
			dp[i][j]=0
print(dp)
print(dp[len(dp)-1][len(dp[0])-1])