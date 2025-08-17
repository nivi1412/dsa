#graph2.py
#given 2 d matrix find if there is way from i(0,0) to i(m*n)
#you can move up and down from O but you cant move if there is X

def DFS(Arr,visited,i,j):
	row=len(Arr)
	col=len(Arr[0])

	if i>= row or i<0 or j<0 or j>= col:
		return 
	if visited[i][j] or matrix[i][j]=='X':
		return 
	else:
		right=DFS(Arr,visited,i+1,j)
		left=DFS(Arr,visited,i-1,j)
		down=DFS(Arr,visited,i,j+1)
		up=DFS(Arr,visited,i,j-1)

		return right or left or down or up



rows=int(input("enter no of rows: "))
Arr=[]
result=False

visited=[[False for _ in range(col)] for _ in range(row)]
print(visited)

for i in range(rows):
	inp=input(f"enter the row{i+1}: ")x
	Arr.append(list(map(int,inp.split())))
for i in range(rows):
	for j in range(len(Arr[0])):
		result=result or DFS(Arr,visited,i,j)

