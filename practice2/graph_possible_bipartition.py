#graph_possible_bipartition.py
import ast
from collections import deque

n=int(input("enter the node count: "))
dislikes=input("enter dislikes array: ")
dislikes=ast.literal_eval(dislikes)
is_bipartition_possible=True
graph={}
color={}
for i in range(n):
	graph[i+1]=[]
	color[i+1]=-1

for pair in dislikes:
	graph[pair[0]].append(pair[1])


q=deque()

q.append(next(iter(graph)))
color[next(iter(graph))]=0

while q:
	node=q.popleft()
	for next_node in graph[node]:
		q.append(next_node)
		if color[next_node]==-1:
			color[next_node]=1-color[node]
		else:
			if color[next_node]==color[node]:
				is_bipartition_possible=False
				break

print(is_bipartition_possible)





