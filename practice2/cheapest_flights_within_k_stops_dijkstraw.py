#cheapest_flights_within_k_stops_dijkstraw.py
import heapq
import ast

n=int(input("no of nodes: "))
flights=input("enter the flights array: ")
flights=ast.literal_eval(flights)

src=int(input("enter the source node: "))
dst=int(input("enter the destination node:"))

k=int(input("enter the stops count:"))

graph={}

for flight in flights:
	if flight[0] not in graph:
		graph[flight[0]]={}
	graph[flight[0]][flight[1]]=flight[2]

print(graph)

h=[]
is_dst_reached=False

heapq.heappush(h,[0,src,k+1])

while h:
	dist,src,stop_count=heapq.heappop(h)
	print("dist,node: ",dist,src,stop_count)
	if stop_count==0:
		if src==dst:
			print(dist)
			is_dst_reached=True
			break
	else:
		for next_node,price in graph[src].items():
			print("stopcount:",k)
			heapq.heappush(h,(dist+price,next_node,stop_count-1))

if not is_dst_reached:
	print(-1)