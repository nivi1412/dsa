#redundant_connections.py
#undirected graph and no cycles
#detect cycle in undirected graph 
#if a node that is visited from a parent node , is being
#visited again with another node than the parent node then there is a cycle in undirected graph

import ast

def detect_cycle(graph,visited,node,answer,parent_node):
	for next_node in graph[node]:
		print("node:",node,next_node,parent_node)
		if visited[next_node]==True and parent_node!=next_node:
			answer.append([next_node,node])
		if visited[next_node]==False:
			visited[next_node]=True
			detect_cycle(graph,visited,next_node,answer,node)

edges=input("enter the edges: ")
edges=ast.literal_eval(edges)

graph={}
new_graph={}
visited={}
answer=[]

print("ng:",new_graph)
for i in range(len(edges)-1,-1,-1):
	if edges[i][0] not in graph:
		graph[edges[i][0]]=[]
		visited[edges[i][0]]=False

	if edges[i][1] not in graph:
		graph[edges[i][1]]=[]
		visited[edges[i][1]]=False

	graph[edges[i][0]].append(edges[i][1])
	graph[edges[i][1]].append(edges[i][0])

print(graph)
print(visited)
node=next(iter(graph))
visited[node]=True
detect_cycle(graph,visited,node,answer,-1)
print(answer)