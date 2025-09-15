#max_profit_Topo_DAG.py

import ast
from collections import deque
import heapq

edges=input("enter the edges: ")
edges=ast.literal_eval(edges)
score=input("enter the time to complete: ")
score=ast.literal_eval(score)

#1.creategraph/inward edge dict

graph={}
inward_edge={}
topo=[]
q=deque()
heap=[]

for edge in edges:
	if edge[0] not in graph:
		graph[edge[0]]=[]
	if edge[0] not in inward_edge:
		inward_edge[edge[0]]=0
	if edge[1] not in graph:
		graph[edge[1]]=[]
	if edge[1] not in inward_edge:
		inward_edge[edge[1]]=0
	inward_edge[edge[1]]+=1
	graph[edge[0]].append(edge[1])
print(graph)
print(inward_edge)

#2.create topological list
for key,value in inward_edge.items():
	if value==0:
		heapq.heappush(heap,(score[key],key))
		q.append(key)

while q:
	node=q.popleft()
	cur_score,cur_node=heapq.heappop(heap)
	topo.append(cur_node)
	for next_node in graph.get(node,[]):
		inward_edge[next_node]-=1
		if inward_edge[next_node]==0:
			q.append(next_node)
			heapq.heappush(heap,(score[next_node],next_node))
print(topo)

#3.calc of score max profit 
max_profit=0
j=1
for i in topo:
	print(i,score[i],i+1)
	max_profit=max_profit+score[i]*j
	j+=1
print("max_profit",max_profit)






