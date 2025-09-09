# DP1_Min_path_sum.py
import ast

Grid=input("enter the Grid: ")
Grid=ast.literal_eval(Grid)

dp=[[0 for _ in range(len(Grid[0]))]for _ in range(len(Grid))]

dp[0][0]=Grid[0][0]

for i in range(1,len(Grid)):
	print("i:",i,Grid[i-1][0],Grid[i][0],Grid[i][0]+Grid[i-1][0])
	dp[i][0]=dp[i-1][0]+Grid[i][0]

for j in range(1,(len(Grid[0]))):
	print("j:",j,Grid[0][j-1],Grid[0][j],Grid[0][j-1]+Grid[0][j])
	dp[0][j]=dp[0][j-1]+Grid[0][j]


for i in range(1,len(Grid)):
	for j in range(1,len(Grid[0])):
		dp[i][j]=min(dp[i-1][j],dp[i][j-1])+Grid[i][j]

print(dp)
print(dp[len(Grid)-1][len(Grid[0])-1])