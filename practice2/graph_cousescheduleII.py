#graph_cousescheduleII.py
import ast

def graph_Course(node,graph,visited,finished,my_list):
	visited[node]=True
	is_cycle_Detected=False
	for next_node in graph[node]:
		if visited[next_node]==True and finished[next_node]==False:
			is_cycle_Detected=True
			break

		if visited[next_node]==False:
			visited[next_node]=True
			is_cycle_Detected=is_cycle_Detected or graph_Course(next_node,graph,visited,finished,my_list)
	finished[node]=True
	return is_cycle_Detected

numcourses=int(input("enter no of courses: "))
prerequisites=input("enter the prerequisites: ")
prerequisites=ast.literal_eval(prerequisites)

graph={}
visited={}
finished={}
is_cycle_Detected=False

if len(prerequisites)==0:
	for i in range(numcourses):
		my_list.append(i)
else:
	for edge in prerequisites:
		if edge[1] not in graph:
			graph[edge[1]]=[]
		graph[edge[1]].append(edge[0])
	for i in range(numcourses):
		if i not in graph:
			graph[i]=[]
		visited[i]=False
		finished[i]=False

	print(graph)
	my_list=[]
	for node in graph:
		if graph_Course(node,graph,visited,finished,my_list):
			is_cycle_Detected=True
			break
		else:
			my_list.append(node)
if is_cycle_Detected:
	print([])
else:
	print(my_list)


