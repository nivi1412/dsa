#longest_increasing_path.py

import ast

def LIP(matrix,memo,i,j,prev_val)->int: # increasing path length 
	a,b,c,d=0,0,0,0
	if i<0 or j<0 or i>len(matrix)-1 or j>len(matrix[0])-1 or matrix[i][j]<=prev_val:
		return 0

	if memo[i][j]!=-1:
		return memo[i][j]

	print("curret,prev:",matrix[i][j],prev_val)

	a+=LIP(matrix,memo,i+1,j,matrix[i][j])
	b+=LIP(matrix,memo,i,j+1,matrix[i][j])
	c+=LIP(matrix,memo,i-1,j,matrix[i][j])
	d+=LIP(matrix,memo,i,j-1,matrix[i][j])

	print("abcd",a,b,c,d)
	memo[i][j]=max(a,b,c,d)
	return 1+memo[i][j]


matrix=input("enter the matrix:")
matrix=ast.literal_eval(matrix)

memo=[[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

path=0

for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		node=matrix[i][j]
		print(matrix[i][j],LIP(matrix,memo,i,j,node))
		path=max(path,LIP(matrix,memo,i,j,-1))

print("path:",path)