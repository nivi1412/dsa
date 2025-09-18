#graph9.py
import ast
from collections import deque

def detect_cycle(node,graph,visited,finished):
	visited[node]=True

	def DFS(node,graph,visited,finished):
		is_cycle_detected = False
		for next_node in graph[node]:
			if finished[next_node]==False and visited[next_node]==True:
				is_cycle_detected=True
			if visited[next_node] is not True:
				visited[next_node]=True
				is_cycle_detected=is_cycle_detected or DFS(next_node,graph,visited,finished)
		finished[node]=True
		return is_cycle_detected

	return DFS(node,graph,visited,finished)

def course_schedule(graph,start_node,BFS_visited):
	q=deque()
	level=0
	q.append([start_node,level])
	BFS_visited[start_node]=True
	result=[]
	while q:
		node,level=q.popleft()
		result.append(node)
		for next_node in graph[node]:
			if BFS_visited[next_node]==False:
				BFS_visited[next_node]=True
				print("next_node",next_node)
				q.append([next_node,level+1])
	return result


numcourses=int(input("enter number of courses:"))
prerequisites=input("enter the prerequisites array:")
prerequisites=ast.literal_eval(prerequisites)

#prerequisite step: make a graph and initialize visited and finished arrays
#step1 : detect if there is a cycle(DFS) if yes retuen courses cant be completed
#step2: if no cycle do BFS
graph={}
visited={}
BFS_visited={}
finished={}
cycle=False
for i in range(len(prerequisites)):
	if prerequisites[i][1] not in graph:
		graph[prerequisites[i][1]]=[]
		visited[prerequisites[i][1]]=False
		BFS_visited[prerequisites[i][1]]=False
		finished[prerequisites[i][1]]=False
	if prerequisites[i][0] not in graph:
		graph[prerequisites[i][0]]=[]
		visited[prerequisites[i][0]]=False
		BFS_visited[prerequisites[i][0]]=False
		finished[prerequisites[i][0]]=False
	graph[prerequisites[i][1]].append(prerequisites[i][0])
print("graph:",graph)


for node in graph:
	if not visited[node]:
		cycle=cycle or detect_cycle(node,graph,visited,finished)
if not cycle:
	for node in graph:
		start_node=node
		if not BFS_visited[start_node]:
			print(course_schedule(graph,start_node,BFS_visited))
else:
	print([])