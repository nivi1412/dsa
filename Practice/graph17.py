#graph17.py
#dikjstraw algorithm

#only for directed graphs with positive edges
import ast
import heapq

rows=5
roadmap=[]
heap=[]
for i in range(rows):
	inp=input(f"enter road: {i+1} ")
	roadmap.append(ast.literal_eval(inp))

print(roadmap)
graph={}
locations_visited={}

#prepare a graph
for roads in roadmap:
	if roads[0] not in graph:
		graph[roads[0]]={}
	graph[roads[0]][roads[1]]=roads[2]

heapq.heappush(heap,[0,next(iter(graph))])
print(graph)
while heap:
	dist,loc=heapq.heappop(heap)
	if loc in locations_visited:
		continue
	locations_visited[loc]=dist
	print(heap)
	for next_loc in graph.get(loc,{}):
		print(next_loc)
		if next_loc not in locations_visited:
			heapq.heappush(heap,[dist+int(graph[loc][next_loc]),next_loc])

print(locations_visited)
