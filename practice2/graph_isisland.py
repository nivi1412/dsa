#graph_isisland.py

def DFS(i,j,grid,visited):
	if i>len(grid)-1 or j > len(grid[0])-1 or i<0 or j<0:
		return

	if grid[i][j]==1 and visited[i][j]==False:
		visited[i][j]=True
		DFS(i+1,j,grid,visited)
		DFS(i-1,j,grid,visited)
		DFS(i,j-1,grid,visited)
		DFS(i,j+1,grid,visited)


row=int(input("enter the row count: "))

grid=[]
island_count=0

for i in range(row):
	Arr=input(f"enter the row {i+1} :")
	Arr=list(map(int,Arr.split()))
	grid.append(Arr)

visited=[[False for _ in range(len(grid[0]))] for _ in range(row)]

for i in range(row):
	for j in range(len(grid[0])):
		if visited[i][j]==False and grid[i][j]==1:
			island_count += 1
			DFS(i,j,grid,visited)

print(island_count)

