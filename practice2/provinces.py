# provinces.py

import ast

def DFS(is_connected,i,j,visited):
	if i>=len(is_connected) or j>=len(is_connected[0]) or i<0 or j<0:
		return

	if visited[i][j]==False and is_connected[i][j]==1:
		visited[i][j]=True
		
		DFS(is_connected,i+1,j,visited)
		DFS(is_connected,i,j+1,visited)
		DFS(is_connected,i-1,j,visited)
		DFS(is_connected,i,j-1,visited)

is_connected=input("enter the array: ")
is_connected=ast.literal_eval(is_connected)
count=0
visited=[[False for _ in range(len(is_connected[0]))]for _ in range(len(is_connected))]


for i in range(len(is_connected)):
	for j in range(len(is_connected[0])):
		if visited[i][j]==False and is_connected[i][j]==1:
			count+=1
			DFS(is_connected,i,j,visited)

print("no of provinces: ",count)