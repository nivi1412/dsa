#evaldivision.py
import ast

def DFS(start,end,graph,visited,mul):
	is_path_found=False
	if start==end:
		print(start,end,mul)
		is_path_found=True
		return mul,is_path_found
	for next_node,val in graph[start].items():
		if visited[next_node]==False:
			visited[next_node]=True
			print("next_node",next_node)
			mul,is_path_found=DFS(next_node,end,graph,visited,mul*val)
	return mul,is_path_found

equations=input("enter the equations: ")
equations=ast.literal_eval(equations)
values=input("enter values array: ")
values=ast.literal_eval(values)
queries=input("enter the array: ")
queries=ast.literal_eval(queries)

graph={}
visited={}
output=[]


for eq,values in zip(equations,values):
	if eq[0] not in graph:
		graph[eq[0]]={}
		visited[eq[0]]=False
	if eq[1] not in graph:
		graph[eq[1]]={}
		visited[eq[1]]=False
	graph[eq[0]][eq[1]]=values
	graph[eq[1]][eq[0]]=round(1/values,6)
visited_copy=visited.copy()
print(graph)

for query in queries:
	start=query[0]
	end=query[1]
	if start==end:
		output.append(1.000000)
	else:
		visited=visited_copy.copy()
		if start in graph and end in graph:
			visited[start]=True
			mul,is_path_found=DFS(start,end,graph,visited,1)
			if is_path_found:
				output.append(mul)
			else:
				output.append(-1.000000)
		else:
			output.append(-1.000000)

print(output)