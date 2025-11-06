#bipartite.py
import ast #abstract syntax tree

def bipartite(node,graph,colour):
	is_bipartite=True
	for next_node in graph[node]:
		if next_node in colour:
			if colour[next_node]==colour[node]:
				return False
		else:
			colour[next_node]=1-colour[node]
			is_bipartite=is_bipartite and bipartite(next_node,graph,colour)

	return is_bipartite



nodes=input("enter the undirected graph nodes: ")
nodes=ast.literal_eval(nodes)

graph={}
for i in range(len(nodes)):
	graph[i]=nodes[i]

print(graph)
colour={}
colour[next(iter(graph))]=0
print(bipartite(next(iter(graph)),graph,colour))