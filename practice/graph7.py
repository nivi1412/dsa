#graph6.py
#detect a cycle in a directed graph

# step1: create a directed graph

def depth_first_search(graph,visited,finished):
	node=graph[0]
	visited[node]=True
	is_cycle_present=False
	def DFS(node):
		for next_node in graph[node]:
			if visited[next_node]==True and finished[next_node]==False:
				is_cycle_present=True
			if visited[next_node]==False:
				visited[next_node]=True
				DFS(next_node)
		finished[node] = True
		return
	DFS(node)


edges=input("enter the edges seperated bu space:")
edges=list(map(int,edges.split()))

graph={}
visited={}
finished={}


def depth_first_search(graph,visited,finished):


for i in range(0,len(edges),+2):
	print(edges[i])
	print(edges[i+1])
	if edges[i] not in graph:
		graph[edges[i]]=[]
		visited[edges[i]]=False
		finished[edges[i]]=False
	if edges[i+1] not in graph:
		graph[edges[i+1]]=[]
		visited[edges[i+1]]=False
		finished[edges[i+1]]=False
	graph[edges[i]].append(edges[i+1])

depth_first_search(graph,visited,finished)

print(graph)
print(visited)
print(finished)
