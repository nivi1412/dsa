#graph_evaluate_division.py
import ast 

def path_exists(startnode,endnode,mul_weight,visited,graph):
	is_destination_reached=False
	if startnode==endnode:
		print(mul_weight)
		is_destination_reached=True
		return mul_weight,is_destination_reached
	else:
		for key,value in graph[startnode].items():
			if visited[key]==False:
				visited[key]=True
				mul_weight,is_destination_reached=path_exists(key,endnode,mul_weight*value,visited,graph)
			if is_destination_reached:
				break
		return mul_weight,is_destination_reached

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
print(graph)
visited_copy=visited.copy()
my_list=[]
for q in queries:
	startnode=q[0]
	endnode=q[1]
	mul_weight=1
	if endnode in graph and startnode in graph:
		visited[startnode]=True
		my_list.append(path_exists(startnode,endnode,mul_weight,visited,graph)[0])
		visited=visited_copy.copy()
	else:
		my_list.append(-1.0)

print(my_list)