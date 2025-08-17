#graph1.py
#breadth first search(part i) consider asyclic part ii) consider cyclic
#edges: [[0,1],[0,3],[0,6],[0,8],[0,10],[1,2],[3,4],[6,7],[9,10]]

import ast
from collections import deque
edges=input("enter the edges of the graph:")
edges=ast.literal_eval(edges)
destination=int(input("enter the destination node: "))
graph={}
q=deque()
is_destinaiton_Reached=False

for edge in edges:
	if edge[0] not in graph:
		graph[edge[0]]=[]
	if edge[1] not in graph:
		graph[edge[1]]=[]
	graph[edge[0]].append(edge[1])
print(graph)
q.append([next(iter(graph.keys())),0])
print("q:",q)
while q:
	val,depth=q.popleft()
	if val == destination:
		print("reached detination node ")
		is_destinaiton_Reached=True
		break
	else:
		for next_val in graph.get(val,[]):
			q.append([next_val,depth+1])

if not is_destinaiton_Reached:
	print("not possible to reach the node")
