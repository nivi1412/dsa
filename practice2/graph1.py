#graph1.py
#breadth first search(part i) consider asyclic part ii) consider cyclic
#edges: [[0,1],[0,3],[0,6],[0,8],[0,10],[1,2],[3,4],[6,7],[9,10]]

import ast
from collections import deque
edges=input("enter the edges of the graph:")
edges=ast.literal_eval(edges)

graph={}
q=deque()

for edge in edges:
	if edge[0] not in graph:
		graph[edge[0]]=[]
	if edge[1] not in graph:
		graph[edge[1]]=[]
	graph[edge[0]].append(edge[1])

q.append([graph[0]])
