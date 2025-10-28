#courseschedule.py
import ast

def DFS(graph,node,visited,finished):
	visited[node]=True
	is_cycle_Detected=False
	for next_node in graph[node]:
		if visited[next_node]==True and finished[next_node]==False:
			is_cycle_Detected=True
		if visited[next_node]==False:
			visited[next_node]=True
			is_cycle_Detected=is_cycle_Detected or DFS(graph,next_node,visited,finished)
		return is_cycle_Detected

	finished[node]=True
	return is_cycle_Detected

numcourses=int(input("enter the course count: "))
prerequisites=input("enter the prerequisites: ")
prerequisites=ast.literal_eval(prerequisites)

graph={}
visited={}
finished={}

for course in prerequisites:
	if course[1] not in graph:
		graph[course[1]]=[]
		visited[course[1]]=False
		finished[course[1]]=False
	if course[0] not in graph:
		graph[course[0]]=[]
		visited[course[0]]=False
		finished[course[0]]=False
	graph[course[1]].append(course[0])
print(graph)
print(not(DFS(graph,next(iter(graph)),visited,finished)))

