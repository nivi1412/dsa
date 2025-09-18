#graph19.py
#Network Delay Time
import ast
import heapq

n=int(input("enter no of nodes: "))
times=input("enter the travel times list: ")
times=ast.literal_eval(times)
k=int(input("enter the start node: "))
graph={}
heap=[]
visited_node={}

for travel_time in times:
	print(travel_time)
	if travel_time[0] not in graph:
		graph[travel_time[0]]=[]
	graph[travel_time[0]].append((travel_time[1],travel_time[2]))
print(graph)
heapq.heappush(heap,[0,k])

while heap:
	dist,node=heapq.heappop(heap)
	if node in visited_node:
		continue
	visited_node[node]=dist
	for next_node,weight in graph.get(node,{}):
		print(next_node,weight)
		heapq.heappush(heap,[dist+int(weight),next_node])
print(visited_node)
min_time = max(visited_node.values())
if len(visited_node)!=n:
	print(-1)
else:
	print(" minimum time it takes for all the n nodes to receive the signal: ",min_time)
