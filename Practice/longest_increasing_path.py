#longest_increasing_path.py

def DFS(Arr,memo,visited,i,j):
	row_len=len(Arr)
	col_len=len(Arr[0])
	left=0
	right=0
	up=0
	down=0

	if memo[i][j]!=-1:
		return memo[i][j]

	if i<0 or i>=row_len or j<0 or j>=col_len:
		return 0

	if visited[i][j]==False:
		visited[i][j]=True
		if 0<=i+1<row_len and Arr[i][j]<Arr[i+1][j]:
			down=DFS(Arr,memo,visited,i+1,j)
		if 0<=j+1<col_len and Arr[i][j]<Arr[i][j+1]:
			right=DFS(Arr,memo,visited,i,j+1)
		if 0<=i-1<row_len and Arr[i][j]<Arr[i-1][j]:
			up=DFS(Arr,memo,visited,i-1,j)
		if 0<=j-1<col_len and Arr[i][j]<Arr[i][j-1]:
			left=DFS(Arr,memo,visited,i,j-1)


	memo[i][j]=1+max(left,right,up,down)
	return memo[i][j]

row=int(input("enter the length of row:"))
col=int(input("enter the length of col:"))
Arr=[]
visited=[]
memo=[[-1 for _ in range(row)] for _ in range(col)]
visited=[[False for _ in range(row)]for _ in range(col)]
for i in range(row):
	inp=input(f"enter row {i+1} values separated by spaces:")
	inp=list(map(int,inp.split()))
	Arr.append(inp)
Max=0
for i in range(row):
	for j in range(col):
		visited=[[False for _ in range(row)]for _ in range(col)]
		Max=max(Max,DFS(Arr,memo,visited,i,j))
print(Max)