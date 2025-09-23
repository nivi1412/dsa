#graph_dikjstaw.py

import ast
import heapq

row=int(input("enter no of rows:"))
roadmap=[]
heap=[]
visited_loc= {}
graph={}
for i in range(row):
	inp=input("enter the distances and locations: ")
	roadmap.append(ast.literal_eval(inp))

for roads in roadmap:
	if roads[0] not in graph:
		graph[roads[0]]=[]
	graph[roads[0]].append((roads[1],roads[2]))
print(graph)

heapq.heappush(heap,[0,next(iter(graph))])

while heap:
	dist,loc=heapq.heappop(heap)
	if loc in visited_loc:
		continue
	visited_loc[loc]=dist
	for next_loc in graph.get(loc,{}):
		if next_loc not in visited_loc:
			heapq.heappush(heap,[dist+int(next_loc[1]),next_loc[0]])

print(visited_loc)
