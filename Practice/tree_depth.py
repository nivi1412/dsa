#find depth of a tree.py
import ast

def find_depth(root_node,graph,visited):
	depth=0
	visited[root_node]=True
	if len(graph[root_node])==0:
		return 0
	for next_node in graph[root_node]:
		if visited[next_node]==False:
			visited[next_node]=True
			depth=max(depth,find_depth(next_node,graph,visited))
	return 1+depth

edges=input("enter the prerequisites array:")
edges=ast.literal_eval(edges)

graph={}
visited={}
min_height=10**5 
result_nodes=[]

for edge in edges:
	if edge[0] not in graph:
		graph[edge[0]]=[]
		visited[edge[0]]=False
	if edge[1] not in graph:
		graph[edge[1]]=[]
		visited[edge[1]]=False
	graph[edge[0]].append(edge[1])
	graph[edge[1]].append(edge[0])

visited_copy=visited.copy()
for key,values in graph.items():
	root_node=key
	visited=visited_copy.copy()
	height=find_depth(root_node,graph,visited)
	if height < min_height:
		result_nodes=[]
		result_nodes.append(root_node)
	if height==min_height:
		result_nodes.append(root_node)
	min_height=min(min_height,height)
print(result_nodes)