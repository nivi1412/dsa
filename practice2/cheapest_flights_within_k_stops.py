#cheapest_flights_within_k_stops.py
import ast

def cheapflight(graph,node,dst,k,cost,visited):
	if dst==node:
		return cost

	if k <0:
		print("node after k stops:",node,cost)
		return float('inf')

	visited.add(node)
	price=float('inf')
	for next_node,val in graph[node].items():
		if next_node not in visited:
			min_price=cheapflight(graph,next_node,dst,k-1,cost+val,visited)
			price=min(min_price,price)

	print("remove node, price till the node:",node, price)
	visited.remove(node)
	return price


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

price=cheapflight(graph,src,dst,k,0,set())

if price==float('inf'):
	print(-1)
else:
	print(price)



