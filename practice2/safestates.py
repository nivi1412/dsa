# safestates.py
import ast

def safestate(node,graph,outdegree,visited,memo):
	if node in memo:
		return memo[node]
	is_safe=True
	next_node=graph.get(node,[])
	if not next_node:
		return True
	for nodes in next_node:
		print("nodes:",nodes)
		if visited[nodes]==True:
			return False
		else:
			visited[nodes]=True
			is_safe=is_safe and safestate(nodes,graph,outdegree,visited,memo)
	memo[node]=is_safe
	return is_safe

edges=input("enter the edges of graph: ")
edges=ast.literal_eval(edges)

graph={}
outdegree={}
visited={}
memo={}

for i in range(len(edges)):
	graph[i]=edges[i]
	visited[i]=False
	if i not in outdegree:
		outdegree[i]=0
	outdegree[i]=len(edges[i])

print(graph)
print(outdegree)
is_safe=True
visited_copy=visited.copy()
fianllist=set()

for node in graph:
	visited=visited_copy.copy()
	visited[node]=True
	if safestate(node,graph,outdegree,visited,memo):
		fianllist.add(node)
print(fianllist)



