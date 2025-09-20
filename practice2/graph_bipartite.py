#graph_bipartite.py

import ast

def DFS(node,graph,color):
	res=True
	print(color)
	for next_node in graph[node]:
		if next_node not in color:
			color[next_node]=1-color[node]
			res=res and DFS(next_node,graph,color)
		elif next_node in color and color[next_node]==color[node]:
			return False
	return res

inp=input("enter the nodes connected to index of the graph: ")
inp=ast.literal_eval(inp)

graph={}
color={}

i=0
for edge in inp:
	if i not in graph:
		graph[i]=[]
	for node in edge:
		graph[i].append(node)
	i+=1
node=next(iter(graph))
color[node]=0
print(DFS(node,graph,color))
