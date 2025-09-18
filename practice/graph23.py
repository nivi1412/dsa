#graph23.py
#bipartite graph

import ast

def dfs(graph,node,color):
	res = True
	
	for next_node in graph[node]:
		if next_node in color:
			if color[next_node] == color[node]:
				return False
		if next_node not in color:
			color[next_node]=1-color[node]
			res = res and dfs(graph, next_node, color)
	return res

inp=input("input graph: ")
inp=ast.literal_eval(inp)

graph={}
color={}
count=0
while(count<len(inp)):
	if count not in graph:
		graph[count]=[]
	for nodes in inp[count]:
		if nodes not in graph:
			graph[nodes]=[]
		if nodes not in graph[count]:
			graph[count].append(nodes)
		if count not in graph[nodes]:
			graph[nodes].append(count)
	count+=1

print(graph)
is_bipartite = True
for node in graph:
	if node in color:
		continue
	color[node] = 0
	is_bipartite = is_bipartite and dfs(graph, node, color)
print(is_bipartite)




