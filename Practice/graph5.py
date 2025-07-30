#graph5.py
#Find if Path Exists in Graph

import ast

def if_path_exists(graph,visited,source,destination):
	node=source
	visited[node]=True
	print("sourcenose",node)

	def DFS(node):
		if node not in graph:
			return False
		if node==destination:
			return True	
		for next_node in graph[node]:
			if visited[next_node]==False:
				visited[next_node]=True
				print(next_node)
				dest_Reached=DFS(next_node)
				if dest_Reached:
					return True
		return False

	return(DFS(node))


edges=input("enter the array of edges:")
edges=ast.literal_eval(edges)
source=int(input("enter the source node:"))
destination=int(input("enter the destination node:"))

edges_dict={}
graph={}
visited={}

for i in edges:
	edges_dict[i[0]]=False
	edges_dict[i[1]]=False
	visited[i[0]]=False
	visited[i[1]]=False

for i in edges:
	if edges_dict[i[0]]==False:
		edges_dict[i[0]]=True
		graph[i[0]]=[]
		graph[i[0]].append(i[1])
	else:
		graph[i[0]].append(i[1])

print(if_path_exists(graph,visited,source,destination))
