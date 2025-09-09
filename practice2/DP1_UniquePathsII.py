#DP1_UniquePathsII.py
import ast

obstacleGrid=input("enter the obstacleGrid: ")
obstacleGrid=ast.literal_eval(obstacleGrid)

dp=[[0 for _ in range(len(obstacleGrid[0]))]for _ in range(len(obstacleGrid))]

for i in range(len(obstacleGrid)):
	dp[i][0]=1 if obstacleGrid[i][0]==0 else 0
for j in range((len(obstacleGrid[0]))):
	dp[0][j]=1 if obstacleGrid[0][j]==0 else 0

for i in range(1,len(obstacleGrid)):
	for j in range(1,len(obstacleGrid[0])):
		dp[i][j]=dp[i-1][j]+dp[i][j-1] if obstacleGrid[i][j]==0 else 0


print(dp)
print(dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1])