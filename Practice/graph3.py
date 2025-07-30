#graph3.py
#BFS
from collections import deque

def BFS(Arr,visited,i,j):

	row=len(Arr)
	col=len(Arr[0])
	q=deque()
	q.append([0,0,0])
	visited[0][0]=True
	while q:
		i,j,dist=q.popleft()

		if i==row-1 and j==col-1:
			if Arr[i][j]=='O':
				visited[i][j]=True
				return dist,True
			else:
				return False

		if 0<=i+1<row and 0<=j<col and Arr[i+1][j]!='X' and visited[i+1][j]==False:
			i=i+1
			visited[i][j]=True
			q.append([i,j,dist+1])
		elif 0<=i<row and 0<=j+1<col and Arr[i][j+1]!='X' and visited[i][j+1]==False:
			j=j+1
			visited[i][j]=True
			q.append([i,j,dist+1])
		else:
			return False


row=int(input("enter no of rows:"))
col=int(input("enter no of cols:"))

Arr=[]
for i in range(row):
	i=input(f"enter the values of row {i+1} :")
	Arr.append(i.split())
print(Arr)

visited =[[False for _ in range(col)] for _ in range(row)]

print(BFS(Arr,visited,i=0,j=0))
