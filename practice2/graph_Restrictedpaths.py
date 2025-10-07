#graph_Restrictedpaths.py
import ast
import heapq

def DFS(graph,min_dist,visited,n,memo,node)->int: #path count

	if node == n:
		return 1
	if node in memo:
		return memo[node]
	dist=0
	for next_node in graph[node]:
		if min_dist[next_node[0]]<min_dist[node]:
			print("node:",node,next_node[0])
			dist=dist+DFS(graph,min_dist,visited,n,memo,next_node[0])
	memo[node]=dist
	return dist


n=int(input("enter no of nodes:"))
edges=input("enter the edges: ")
edges=ast.literal_eval(edges)

graph={}
min_dist={}
visited={}
memo={}
h=[]

for edge in edges:
	if edge[0] not in graph:
		graph[edge[0]]=[]
		# min_dist[edge[0]]=100001
		visited[edge[0]]=False
	if edge[1] not in graph:
		graph[edge[1]]=[]
		# min_dist[edge[1]]=100001
		visited[edge[1]]=False
	graph[edge[0]].append((edge[1],edge[2]))
	graph[edge[1]].append((edge[0],edge[2]))

print(graph)

heapq.heappush(h,[0,n])

while h:
	dist,node=heapq.heappop(h)
	if node not in min_dist:
		min_dist[node]=dist
	for next_node in graph[node]:
		if next_node[0] not in min_dist:
			heapq.heappush(h,[next_node[1]+dist,next_node[0]])

min_dist=dict(sorted(min_dist.items()))
print(min_dist)

print(DFS(graph,min_dist,visited,n,memo,1))

