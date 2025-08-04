import ast
from collections import deque

def is_cycle_present(node,graph,visited,finished):
	cycle=False
	visited[node]=True
	for next_node in graph[node]:
		if finished[next_node]==False and visited[next_node]==True:
			cycle=True
			return cycle
		if visited[next_node]==False:
			visited[next_node]=True
			cycle =cycle or is_cycle_present(next_node,graph,visited,finished)
	finished[node]=True
	return cycle

def course_schedule(q,graph,BFS_visited):
	result=[]
	while q:
		node,level=q.popleft()
		result.append(node)	
		# print("node:",node,graph[node])
		for next_node in graph[node]:
			if BFS_visited[next_node]==False:
				BFS_visited[next_node]=True
				q.append([next_node,level+1])
	return result

numcourses=int(input("enter number of courses:"))
prerequisites=input("enter the prerequisites array:")
prerequisites=ast.literal_eval(prerequisites)

graph={}
visited={}
BFS_visited={}
finished={}
inward_degree={}
cycle=False

for i in range(len(prerequisites)):
	if prerequisites[i][1] not in graph:
		graph[prerequisites[i][1]]=[]
		visited[prerequisites[i][1]]=False
		BFS_visited[prerequisites[i][1]]=False
		finished[prerequisites[i][1]]=False
		inward_degree[prerequisites[i][1]]=0
	if prerequisites[i][0] not in graph:
		graph[prerequisites[i][0]]=[]
		visited[prerequisites[i][0]]=False
		BFS_visited[prerequisites[i][0]]=False
		finished[prerequisites[i][0]]=False
		inward_degree[prerequisites[i][0]]=0
	graph[prerequisites[i][1]].append(prerequisites[i][0])

inward_nodes=[]

for keys,values in graph.items():
	for i in values:
		inward_degree[i]+=1
print(inward_degree)
for key,values in inward_degree.items():
	if values==0:
		inward_nodes.append(key)

print("inward_nodes",inward_nodes)
for node in inward_nodes:
	cycle=cycle or is_cycle_present(node,graph,visited,finished)

if not cycle:
	q=deque()
	for node in inward_nodes:
		if BFS_visited[node] == False:
			q.append([node,0])
			BFS_visited[node]=True
	print(course_schedule(q,graph,BFS_visited))



