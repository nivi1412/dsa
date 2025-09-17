#graph25.py
#find all paths
import ast

#[[1,3],[3,4],[3,5],[3,6]]

def find_paths(node,graph):
	result=[]
	path=[]
	finished_nodes=set()
	def DFS(node):
		nonlocal result
		nonlocal path
		
		path.append(node)
		finished_nodes.add(node)

		neighbour_node=graph.get(node,[])
		if not neighbour_node:	
			result.append(path.copy())
		else:
			for v in neighbour_node:
				if v in finished_nodes:
					continue
				DFS(v)
		path.pop()

	DFS(node)
	print("result:",result)
	return result

edges=input("enter the edges: ")
edges=ast.literal_eval(edges)

graph={}

for edge in edges:
	if edge[0] not in graph:
		graph[edge[0]]=[]
	if edge[1] not in graph:
		graph[edge[1]]=[]

	graph[edge[0]].append(edge[1])
print(graph)
for node in graph:
	print(find_paths(node,graph))









