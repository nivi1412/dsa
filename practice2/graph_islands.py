# graph_islands.py

# You are given an m x n grid filled with:

# '1' → land

# '0' → water

# An island is formed by connecting adjacent lands ('1') horizontally or vertically (not diagonally).
# You need to count the number of islands.

def DFS(Arr,visited,i,j):
	row=len(Arr)
	col=len(Arr[0])
	if i<0 or j<0 or i>row-1 or j>col-1:
		return
	if visited[i][j] or Arr[i][j]==0:
		return
	else:
		if Arr[i][j]==1:
			visited[i][j]=True
		DFS(Arr,visited,i+1,j)
		DFS(Arr,visited,i-1,j)
		DFS(Arr,visited,i,j+1)
		DFS(Arr,visited,i,j-1)

row=int(input("enter the length of row: "))
Arr=[]
for i in range(row):
	inp=input("enter the values:")
	Arr.append(list(map(int,inp.split())))

visited=[[False for _ in range(len(Arr[0]))] for _ in range(len(Arr))]
is_island=0
for i in range(len(Arr)):
	for j in range(len(Arr[0])):
		if Arr[i][j]==1 and visited[i][j]==False:
			print(i,j)
			is_island+=1
			DFS(Arr,visited,i,j)
print(is_island)
