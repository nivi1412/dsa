#graph_evaluate_division.py
import ast 

def path_exists(startnode,endnode,mul_weight,visited,graph):
	if startnode==endnode:
		return mul_weight
	else:
		if visited[startnode]==False:
			visited[startnode]=True
			for key,value in graph[startnode].items():
				mul_weight=mul_weight*value
				return path_exists(key,endnode,mul_weight,visited,graph)




equations=input("enter the equations: ")
equations=ast.literal_eval(equations)
values=input("enter values: ")
values=ast.literal_eval(values)
queries=input("enter the queries: ")
queries=ast.literal_eval(queries)

graph={}
visited={}

for edge,value in zip(equations,values):
	if edge[0] not in graph:
		graph[edge[0]]={}
		visited[edge[0]]=False
	if edge[1] not in graph:
		graph[edge[1]]={}
		visited[edge[1]]=False
	graph[edge[0]][edge[1]]=value
	graph[edge[1]][edge[0]]=round(1/value,5)

visited_copy=visited.copy()
my_list=[]
for q in queries:
	startnode=q[0]
	endnode=q[1]
	mul_weight=1
	if endnode in graph and startnode in graph:
		my_list.append(path_exists(startnode,endnode,mul_weight,visited,graph))
		visited=visited_copy.copy()
	else:
		my_list.append(-1.0)

