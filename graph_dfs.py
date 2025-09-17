#graph_DFS.py
#depth first search first go to edge till end and backtrack to origin vertex

# Solved for directed acyclic graphs
# Now solve for directed cyclic graphs

def DFS(node,parent):
	if not visited[node]:
		visited[node]=True
		for i in graph[node]:
			# if i==parent:
			# 	pass
			if not visited[i]:
				print("neighbour,parent:",i,node)
				DFS(i,node)
			elif i!=parent and parent!=-1:
				print("DAG is detected at node,neighbour,parent:",node,i,parent)

# 0 - 1 - 2 - 3 - 4 - 0
# (0, -1)
# (1, 0)
# (2, 1)
# (3, 2)
# (4, 3)

# 0 - 1 - 3
# 0 - 2 - 3

Arr=input("enter the edges sep by spaces:")
Arr=list(map(int,Arr.split()))

graph={}
visited={}

for i in range(0,len(Arr),2):
	u=Arr[i]
	v=Arr[i+1]
	if u not in graph:
		graph[u]=[]
	if v not in graph:
		graph[v]=[]

	graph[u].append(v)
	# graph[v].append(u)
	visited[u]=False
	visited[v]=False	

for node in graph:
	print(f"{node}:{graph[node]}")
print(visited)
parent=-1
for node in graph:
	if not visited[node]:
		DFS(node,parent)