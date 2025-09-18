#graph2.py
#given 2 d matrix find if there is way from i(0,0) to i(m*n)
#you can move up and down from O but you cant move if there is X

def DFS(matrix,visited,i,j):
	row=len(matrix)
	col=len(matrix[0])

	if i<0 or i>=row or j<0 or j>=col:
		return

	if visited[i][j] or matrix[i][j]=='X':
		return

	visited[i][j]=True
	print(f"visited: ({i},{j} --> {matrix[i][j]})")

	DFS(matrix,visited,i-1,j)
	DFS(matrix,visited,i+1,j)
	DFS(matrix,visited,i,j-1)
	DFS(matrix,visited,i,j+1)

	return visited


row=int(input("enter no of rows:"))
col=int(input("enter no of cols:"))

matrix=[]

for i in range(row):
	inp=input("enter the rows seperated by spaces")
	inp=list(inp.split())
	matrix.append(inp)

# start_node=(0,0)
# end_node=(row-1,col-1)

visited=[[False for _ in range(col)] for _ in range(row)]
print(visited)

updated_visited=DFS(matrix,visited,0,0)
new_row=len(updated_visited)
new_col=len(updated_visited)

if updated_visited[new_row-1][new_col-1]==False:
	print("False")
else:
	print("True")


