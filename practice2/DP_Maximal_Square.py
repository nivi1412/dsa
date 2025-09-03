# DP_Maximal Square.py

import ast
matrix=input("enter matrix: ")
matrix=ast.literal_eval(matrix)
matrix = [[int(x) for x in row] for row in matrix]

dp=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
max_val=0

for i in range(len(matrix)):
	if matrix[i][0]==1:
		dp[i][0]=1 
for j in range(len(matrix[0])):
	if matrix[0][j]==1:
		dp[0][j]=1 

for i in range(1,len(matrix)):
	for j in range(1,len(matrix[0])):
		if matrix[i][j]==1:
			dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
		if dp[i][j]>max_val:
			max_val=dp[i][j]

print(max_val*max_val)

