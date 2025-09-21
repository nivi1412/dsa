#graph_Redundant_connectionII.py

import ast

def detect_cycle(node,graph,visited,finished,my_list):
	for next_node in graph[node]:
		if finished[next_node]==False and visited[next_node]==True:
			my_list.append([node,next_node])
		if visited[next_node]==False:
			visited[next_node]=True
			detect_cycle(next_node,graph,visited,finished,my_list)
	finished[node]=True


edges=input("enter the edge list of DG:")
edges=ast.literal_eval(edges)

graph={}
visited={}
finished={}
indegree={}
candidate=[]

for edge in edges:
	if edge[0] not in graph:
		graph[edge[0]]=[]
		visited[edge[0]]=False
		finished[edge[0]]=False
		indegree[edge[0]]=0	
	if edge[1] not in graph:
		graph[edge[1]]=[]
		visited[edge[1]]=False
		finished[edge[1]]=False
		indegree[edge[1]]=0
	graph[edge[0]].append(edge[1])
	indegree[edge[1]]+=1
	if indegree[edge[1]]==2:
		candidate.append([edge[0],edge[1]])


print(graph)
print(indegree)

node=next(iter(graph))
visited[node]=True
my_list=[]
detect_cycle(node,graph,visited,finished,my_list)

final_list=[]
if candidate:
	for i in candidate:
		if i in my_list:
			final_list.append(i)
else:
	final_list.append(my_list[-1])

if not final_list:
		final_list.append(candidate[-1])

print(final_list[-1])



