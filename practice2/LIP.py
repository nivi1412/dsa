#LIP.py
import ast

def LIP(i,j,matrix,prev_value,dp):
	# if (i,j) in dp:
	# 	return dp[(i,j)]
	if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]):
		return 0
	if prev_value !=None and matrix[i][j] <= prev_value:
		return 0

	down=LIP(i+1,j,matrix,matrix[i][j],dp)
	right=LIP(i,j+1,matrix,matrix[i][j],dp)
	up=LIP(i-1,j,matrix,matrix[i][j],dp)
	left=LIP(i,j-1,matrix,matrix[i][j],dp)
	
	return 1+max(left,right,up,down)


matrix=input("enter the matrix: ")
matrix=ast.literal_eval(matrix)
pathlength=0
dp={}


for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		pathlength=max(pathlength,LIP(i,j,matrix,None,dp))

print(pathlength)