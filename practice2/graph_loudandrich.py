# graph_loudandrich.py
import ast

def loudrich(node,visited,graph,quiet,memo,min_loud):
	neighbour_node=graph.get(node,[])
	if not neighbour_node:
		memo[node]=min(min_loud,quiet[node])
	else:
		for v in neighbour_node:
			if visited[v]==False:
				visited[v]=True
				# min_loud=min(min_loud,quiet[node])
				min_loud=min(loudrich(v,visited,graph,quiet,memo,min_loud),min_loud)
		memo[node]=min_loud
	return memo[node]

richer=input("enter the rich relation: ")
richer=ast.literal_eval(richer)
quiet=input("enter the quiet array: ")
quiet=ast.literal_eval(quiet)

graph={}
visited={}
memo={}
final_list=[]

for edge in richer:
	if edge[0] not in graph:
		graph[edge[0]]=[]
		visited[edge[0]]=False
		memo[edge[0]]=0
	if edge[1] not in graph:
		graph[edge[1]]=[]
		visited[edge[1]]=False
		memo[edge[1]]=0
	graph[edge[1]].append(edge[0])

graph=dict(sorted(graph.items()))
visited_copy=visited.copy()
for node in graph:
	print("==================",node)
	visited=visited_copy.copy()
	visited[node]=True
	min_loud=quiet[node]
	final_list.append(quiet.index(loudrich(node,visited,graph,quiet,memo,min_loud)))
print(final_list)