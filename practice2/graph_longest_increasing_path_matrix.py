#graph_longest_Incresing_path_matrix.py

import ast

def LIP(i,j,matrix,memo,prev_value):
	count1,count2,count3,count4=0,0,0,0

	if i>len(matrix)-1 or j >len(matrix[0])-1 or i<0 or j<0:
		return 0

	if matrix[i][j]<=prev_value:
		return 0
		
	if memo[i][j]!=-1:
		return memo[i][j]

	count1=LIP(i+1,j,matrix,memo,matrix[i][j])
	count2=LIP(i,j+1,matrix,memo,matrix[i][j])
	count3=LIP(i-1,j,matrix,memo,matrix[i][j])
	count4=LIP(i,j-1,matrix,memo,matrix[i][j])

	memo[i][j]=1+max(count1,count4,count3,count2)
	return memo[i][j]

matrix=input("enter the matraix: ")
matrix=ast.literal_eval(matrix)
count=0
memo=[[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
print(memo)
print(matrix)

for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		count=max(count,LIP(i,j,matrix,memo,-1))
		print("count:",i,j,count)

print(count)