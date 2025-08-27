# DP_Unique_paths.py

def uniquepaths(grid,row,col)->int:
	count=0
	def DFS(grid,row,col):
		nonlocal count
		if row<0 or col<0 or row>len(grid) or col>len(grid[0]):
			return 
		if row==len(grid) and col==len(grid[0]):
			count+=1
		DFS(grid,row+1,col)
		DFS(grid,row,col+1)


m=int(input("enter no of rows: "))
n=int(input("enter no of cols: "))

grid=[[0 for _ in range(n)] for _ in range(m)]

print(grid)


uniquepaths(grid,row=0,col=0)