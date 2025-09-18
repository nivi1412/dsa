#graph14.py
#Number of Provinces

#list of elements should be given to array matrix
#in not iin
#increment should be done for a province at the start of DFS for unvisited node
#check for edge and then check for visited or not 
#isconnected[start_node][next_node] this should be in matrix form and not list form

def DFS(start_node,isconnected,visited):
	for next_node in range(len(isconnected[0])):
		if isconnected[start_node][next_node]==1:
			if visited[next_node]==False:
				visited[next_node]=True
				DFS(next_node,isconnected,visited)

rows=int(input("enter no of rows:"))
cols=int(input("enter no of cols:"))

isconnected=[]
province=0
for i in range(rows):
	inp=input(f"enter the edge value if {i+1} row")
	isconnected.append(list(map(int,inp.split())))
visited=[False for _ in range(rows)]
print(isconnected)
for i in range(rows):
	start_node=i
	if visited[start_node]==False:
		visited[start_node]=True
		province+=1
		DFS(start_node,isconnected,visited)
print(province)

