# graph_clonegraph.py
import ast

class clone:
	def __init__(self,data):
		self.data=data
		self.neighbour=[]

def clonegraph(node,graph,visited):
	if node in visited:
		return visited[node]

	cur_node=clone(node)
	visited[node]=cur_node

	for next_node in graph[node]:
		cur_node.neighbour.append(clonegraph(next_node,graph,visited))

	return cur_node

def print_graph(node,seen=set()):
	if node in seen:
		return
	seen.add(node)
	print(f"Node {node.data} -> {[n.data for n in node.neighbour]}")
	for n in node.neighbour:
		print_graph(n,seen)

adjlist=input("enter adjacency list: ")
adjlist=ast.literal_eval(adjlist)

graph={}
visited={}

for i in range(len(adjlist)):
	graph[i+1]=adjlist[i]

node=next(iter(graph))
node=clonegraph(node,graph,visited)
print_graph(node)