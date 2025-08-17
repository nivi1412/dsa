#graph4.py
#detect a cycle in a directed graph

import ast

def is_cycle_present(node,graph,visited,finished):
	visited[node]=True
	cycle=False
	def DFS(node,graph,visited,finished):
		nonlocal cycle
		for next_node in graph[node]:
			if finished[next_node]==False and visited[next_node]==True:
				return True
			if visited[next_node]==False:
				visited[next_node]=True
				cycle=cycle or DFS(next_node,graph,visited,finished)
		finished[node]=True
		return cycle
	return 	DFS(node,graph,visited,finished)

edges=input("enter the edges of a DAG: ")
edges=ast.literal_eval(edges)

graph={}
visited={}
finished={}
cycle=False

for edge in edges:
	if edge[0] not in graph:
		graph[edge[0]]=[]
		visited[edge[0]]=False
		finished[edge[0]]=False
	if edge[1] not in graph:
		graph[edge[1]]=[]
		visited[edge[1]]=False
		finished[edge[1]]=False
	
	graph[edge[0]].append(edge[1])
print(graph)
for node in graph:
	if is_cycle_present(node,graph,visited,finished):
		print(True)
		cycle=True
		break
if not cycle:
	print(False)