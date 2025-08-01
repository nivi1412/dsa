#graph6.py

import ast	

input_node=input("enter the array of edges:")
input_node=ast.literal_eval(input_node)

edges={}
graph={}
degree={}

for i in input_node :
	if i[1] not in graph:
		graph[i[1]]=[]
	if i[0] not in graph:
		graph[i[0]]=[]
	graph[i[0]].append(i[1])
	graph[i[1]].append(i[0])


for key,value in graph.items():
	if len(value)==len(graph)-1:
		print(key)

