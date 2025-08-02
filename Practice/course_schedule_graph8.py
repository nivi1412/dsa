#course_schedule(graph8).py
import ast

def detectcycle(graph,visited,finished):
	print(graph)
	node=list(graph.keys())[0]
	visited[node]=True
	is_cycle_detected=False
	course_order=[]

	def DFS(node,visited,finished):
		nonlocal is_cycle_detected
		for next_node in graph[node]:
			if visited[next_node]==True and finished[next_node]==False:
				is_cycle_detected=True
				return is_cycle_detected
			if visited[next_node]==False:
				visited[next_node]=True
				DFS(next_node,visited,finished)
		finished[node]=True
		print(node)

	for node in graph.keys():
		if not visited[node]:
			DFS(node, visited, finished)

	return not is_cycle_detected


numCourses=int(input("enter the number of courses:"))
edges=input("enter the edge list")
edges=ast.literal_eval(edges)
graph={}
visited={}
finished={}


for i in range(len(edges)):
	if edges[i][0] not in graph:
		graph[edges[i][0]]=[]
	if edges[i][1] not in graph:
		graph[edges[i][1]]=[]
	graph[edges[i][1]].append(edges[i][0])
	visited[edges[i][0]]=False
	visited[edges[i][1]]=False
	finished[edges[i][0]]=False
	finished[edges[i][1]]=False


print(detectcycle(graph,visited,finished))