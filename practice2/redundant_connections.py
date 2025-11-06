# redundant_connections.py

import ast

def redundant_connections(node,graph,visited,ans,parent_node):
	for next_node in graph[node]:
		if visited[next_node]==True and parent_node!=next_node:
			ans.append([next_node,node])
			return
		if visited[next_node]==False:
			visited[next_node]=True
			return redundant_connections(next_node,graph,visited,ans,node)

edges=input("enter the edges of the graph:")
edges=ast.literal_eval(edges)

graph={}
visited={}

for edge in edges:
	if edge[0] not in graph:
		graph[edge[0]]=[]
		visited[edge[0]]=False
	if edge[1] not in graph:
		graph[edge[1]]=[]
		visited[edge[1]]=False

	graph[edge[0]].append(edge[1])
	graph[edge[1]].append(edge[0])

print(graph)
node=next(iter(graph))
visited[node]=True
ans=[]
redundant_connections(node,graph,visited,ans,None)
print(ans)