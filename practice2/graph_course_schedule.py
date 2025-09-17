#graph_courseschedule.py

import ast

def detect_cycle(node,graph,visited,finished):
	visited[node]=True
	print("node:",node)
	is_cycle_Detected=False
	for next_node in graph[node]:
		if visited[next_node]==True and finished[next_node]==False:
			is_cycle_Detected=True
			break
		if visited[next_node]==False:
			visited[next_node]=True
			is_cycle_Detected=is_cycle_Detected or detect_cycle(next_node,graph,visited,finished)
	finished[node]=True
	return is_cycle_Detected

numcourses=input("enter no of courses: ")
prerequisites=input("enter the prerequisites: ")
prerequisites=ast.literal_eval(prerequisites)

graph={}
visited={}
finished={}
is_cycle_Detected=False

for edge in prerequisites:
	if edge[1] not in graph:
		graph[edge[1]]=[]
		visited[edge[1]]=False
		finished[edge[1]]=False
	if edge[0] not in graph:
		graph[edge[0]]=[]
		visited[edge[0]]=False
		finished[edge[0]]=False
	graph[edge[1]].append(edge[0])
	print(graph)

print(graph)
for node in graph:
	if detect_cycle(node,graph,visited,finished):
		is_cycle_Detected=True
		break
print(is_cycle_Detected)



