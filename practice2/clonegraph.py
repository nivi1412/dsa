# clonegraph.py
import ast

class Node():
	def __init__(self,value=None,neighbour=None):
		self.value=value
		self.neighbour=neighbour if neighbour is not None else []

def clonegraph(graph,node,visited):
	if visited[node]:
		return visited[node]
	cur_node=Node(node)
	visited[node]=cur_node

	for neighbour in graph[node]:
		if visited[neighbour]==False:
			cur_node.neighbour.append(clonegraph(graph,neighbour,visited))
		else:
			cur_node.neighbour.append(visited[neighbour])

	return cur_node

def print_graph(node,seen=set()):
	if node in seen:
		return
	seen.add(node)
	print("seen:",seen)
	print(f"Node {node.value} -> {[n.value for n in node.neighbour]}")
	for n in node.neighbour:
		print_graph(n,seen)

adjlist=input("enter adjacency list: ")
adjlist=ast.literal_eval(adjlist)

graph={}
visited={}
new_visited={}

for i in range(len(adjlist)):
	graph[i+1]=adjlist[i]
	visited[i+1]=False
	new_visited[i+1]=False

print(graph)

cloned=clonegraph(graph,next(iter(graph)),visited)
print_graph(cloned)
