#graph_topologicalsort.py
import ast
from collections import deque

edges=input("enter the edges: ")
edges=ast.literal_eval(edges)
time=input("enter the time to complete: ")
time=ast.literal_eval(time)

graph={}
q=deque()
inward_edge={}
topo=[]
dp=[]

for edge in edges:
	print(edge[0],edge[1])
	if edge[0] not in inward_edge:
		inward_edge[edge[0]]=0
	if edge[1] not in inward_edge:
		inward_edge[edge[1]]=0
	if edge[0] not in graph:
		graph[edge[0]]=[]
	graph[edge[0]].append(edge[1])	
	inward_edge[edge[1]]+=1

inward_edge_copy=inward_edge.copy()

for key,values in inward_edge_copy.items():
	if values==0:
		q.append(key)
while q:
	node=q.popleft()
	topo.append(node)
	for vertices in graph.get(node,[]):
		inward_edge_copy[vertices]-=1
		if inward_edge_copy[vertices]==0:
			q.append(vertices)

dp=[0 for _ in range(len(topo))]
dp[0]=time[0]
for i in range(1,len(topo)):

	if inward_edge[topo[i-1]]==inward_edge[topo[i]]:
		dp[i]=max(time[i],dp[i-1])
	else:

		dp[i]=dp[i-1]+int(time[i])

print(dp[-1])





