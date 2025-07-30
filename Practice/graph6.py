#graph6.py

import ast

def find_center_stargraph(graph,edges,degree):
	print(graph)
	node=list(graph.keys())[0]
	edges[node]=True
	def DFS(node):
		if node not in graph:
			return 
		for next_node in graph[node]:
			print("next_node",next_node)
			print(edges[node])
			if edges[next_node]==False:
				edges[next_node]=True
				print("nodevalue:",next_node)
				degree[next_node]+=1
				degree[node]+=1
				DFS(next_node)
	DFS(node)
	return degree

	

input_node=input("enter the array of edges:")
input_node=ast.literal_eval(input_node)

visited={}
edges={}
graph={}
degree={}
for i in input_node:
	visited[i[0]]=False
	visited[i[1]]=False
	edges[i[0]]=False
	edges[i[1]]=False
	degree[i[0]]=0
	degree[i[1]]=0

for i in input_node :
	if visited[i[0]]==False:
		visited[i[0]]=True
		graph[i[0]]=[]
		graph[i[0]].append(i[1])
	else:
		graph[i[0]].append(i[1])


degree=find_center_stargraph(graph,edges,degree)
Max=list(degree.values())[0]
print(degree)
for key,value in degree.items():
	if value>Max:
		Max=value
		star_node=key
print(star_node)

