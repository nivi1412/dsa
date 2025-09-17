#graph16.py
#Redundant Connection

import ast

def detect_cycle(start_node,graph,visited,finished):
	cycle = []
	for next_node in graph[start_node]:
		if finished[next_node]==False and visited[next_node]==True:
			return [True,start_node,next_node]
		if visited[next_node]==False:
			visited[next_node]=True
			cycle.extend(detect_cycle(next_node,graph,visited,finished))
	finished[start_node]=True
	print(cycle)
	return cycle

edges=input(" enter the edges: ")
edges=ast.literal_eval(edges)

graph={}
visited={}
finished={}
result=[]

for edge in edges:
	print(edge[0],edge[1])
	if edge[0] not in graph:
		graph[edge[0]]=[]
		visited[edge[0]]=False
		finished[edge[0]]=False
	if edge[1] not in graph:
		graph[edge[1]]=[]
		visited[edge[1]]=False
		finished[edge[1]]=False

	graph[edge[0]].append(edge[1])
	graph[edge[1]].append(edge[0])

	# has_cycle = False
	start_node=next(iter(graph))
	if not visited[start_node]:
		visited[start_node] = True
		cycle=detect_cycle(start_node, graph, visited, finished)
		print(cycle)

        # if cycle(0):
        # 	result.append(cycle(1),cycle(2))
	            
print(result)


