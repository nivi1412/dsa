# graph_findallpaths.py
import ast

def findallpaths(node,graph,visited)->list:
	answer=[]
	visited[node]=True
	local=[]
	def DFS(node,graph,visited):
		nonlocal answer
		nonlocal local

		local.append(node)
		neighbour_nodes=graph.get(node,[])
		if not neighbour_nodes:
			answer.append(local.copy())
		else:
			for v in neighbour_nodes:
				if visited[v]==True:
					continue
				DFS(v,graph,visited)
		local.pop()

	DFS(node,graph,visited)
	return answer


edges=input("enter the edges of the directed graph:")
edges=ast.literal_eval(edges)

graph={}
visited={}
ans=[]

for edge in edges:
	if edge[0] not in graph:
		graph[edge[0]]=[]
		visited[edge[0]]=False
	if edge[1] not in graph:
		graph[edge[1]]=[]
		visited[edge[1]]=False
	graph[edge[0]].append(edge[1])

# for node in graph:
ans.append(findallpaths(next(iter(graph)),graph,visited))
print(ans)
