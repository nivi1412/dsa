# graph_loudandrich.py
import ast

def loudandrich(node,graph,quiet)->int:
	prev_min=quiet[node]
	def DFS(node,graph,quiet):
		nonlocal prev_min
		for next_node in graph[node]:
			# print("before:",node,next_node,prev_min)
			prev_min=quiet[next_node] if prev_min > quiet[next_node] else prev_min
			# print("after:",node,next_node,prev_min)
			DFS(next_node,graph,quiet)

	DFS(node,graph,quiet)
	return prev_min

richer=input("enter the richer array:")
richer=ast.literal_eval(richer)
quiet=input("enter the quiet array:")
quiet=ast.literal_eval(quiet)

graph={}
visited={}
my_list=[]
for edge in richer:
	if edge[0] not in graph:
		graph[edge[0]]=[]
		visited[edge[0]]=False
	if edge[1] not in graph:
		graph[edge[1]]=[]
		visited[edge[1]]=False
	graph[edge[1]].append(edge[0])

for node in sorted(graph.keys()):
	if not visited[node]:
		visited[node]=True
		my_list.append(quiet.index(loudandrich(node,graph,quiet)))
print(my_list)