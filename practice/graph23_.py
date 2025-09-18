#graph23_.py
import ast

inp=input("input graph: ")
inp=ast.literal_eval(inp)

def dfs(graph,node,set_A,set_B):
	is_biparted=True
	print(set_A,set_B)
	print("node",node)
	for next_node in graph[node]:
		if next_node not in set_A and next_node not in set_B:
			if node in set_A:
				set_B.add(next_node)
			else:
				set_A.add(next_node)
			is_biparted=is_biparted and dfs(graph,next_node,set_A,set_B)
		elif (next_node in set_A and node in set_A) or (next_node in set_B and node in set_B):
			print("im here")
			return False
	return is_biparted 

graph={}
count=0

while(count<len(inp)):
	if count not in graph:
		graph[count]=[]
	for nodes in inp[count]:
		if nodes not in graph:
			graph[nodes]=[]
		if nodes not in graph[count]:
			graph[count].append(nodes)
		if count not in graph[nodes]:
			graph[nodes].append(count)
	count+=1
print(graph)
set_A=set()
set_B=set()

set_A.add(next(iter(graph)))

print(dfs(graph,next(iter(graph)),set_A,set_B))
