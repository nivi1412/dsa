#DP_Min_Path_sum.py
import ast

def minpathsum(dp,grid,m,n)->int:	
	print(dp)
	print("m,n:",m,n)
	if dp[m][n]:
		return dp[m][n]
	if n<0 or m<0:
		return 0
	if m==0:
		return minpathsum(dp,grid,0,n-1)+grid[0][n]
	if n==0:
		return minpathsum(dp,grid,m-1,0)+grid[m][0]
	dp[m][n]=grid[m][n]+min(minpathsum(dp,grid,m,n-1),minpathsum(dp,grid,m-1,n))
	return dp[m][n]


grid=input("enter the grid matrix:")
grid=ast.literal_eval(grid)

dp=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

dp[0][0]=grid[0][0]

#top down

print(minpathsum(dp,grid,m=len(grid)-1,n=len(grid[0])-1))


#bottoms up
# for i in range(1,len(grid)):
# 	dp[i][0]=dp[i-1][0]+grid[i][0]

# for j in range(1,len(grid[0])):
# 	dp[0][j]=dp[0][j-1]+grid[0][j]

# print(dp)
# for i in range(1,len(grid)):
# 	for j in range(1,len(grid[0])):
# 		dp[i][j]=grid[i][j]+min(dp[i][j-1],dp[i-1][j])
# print(dp[len(grid)-1][len(grid[0])-1])
