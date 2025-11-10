# loudandrich.py

import ast

def loudrich(graph,node,quiet,min_val):
	for next_node in graph[node]:
		if quiet[next_node]<min_val:
			min_val=quiet[next_node]
		min_val=loudrich(graph,next_node,quiet,min_val)
	return min_val

richer=input("enter the richer array: ")
richer=ast.literal_eval(richer)
quiet=input("enter the quiet array: ")
quiet=ast.literal_eval(quiet)

graph={}

for rich in richer:
	if rich[1] not in graph:
		graph[rich[1]]=[]
	if rich[0] not in graph:
		graph[rich[0]]=[]
	graph[rich[1]].append(rich[0])

graph={key:value for key,value in sorted(graph.items())}
print(graph)

finallist=[]
for node in graph:
	min_val=quiet[node]
	min_val=loudrich(graph,node,quiet,min_val)
	finallist.append(quiet.index(min_val))
print(finallist)
