#graph21_practice.py
# Cheapest Flights Within K Stops
import ast 
import heapq

n=int(input("no of cities: "))
flights=input("enter the flights array: ")
flights=ast.literal_eval(flights)
src=int(input("enter the source node: "))
dst=int(input("enter the destination node: "))
k=int(input("enter no of atmost stops from source to destination: "))

route_map={}
cheapestflights={}
heap=[]

for nodes in flights:
	if nodes[0] not in route_map:
		route_map[nodes[0]]={}
	route_map[nodes[0]][nodes[1]]=nodes[2]

heapq.heappush(heap,[0,src,0])

while heap:
	price,node,stop_count=heapq.heappop(heap)

	if node not in cheapestflights:
		cheapestflights[node]={}
	if stop_count in cheapestflights[node]
		continue
	cheapestflights[node][stop_count]=price

	for next_node,next_price in route_map.get(node,{}).items:
		if stop_count <=k+1
		heapq.heappush(heap,[price+next_price,next_node,stop_count+1])

min_price=10**5
for node_count,price in cheapestflights[dst].items():
	if node_count-1 <= k:
		if price<min_price:
			min_price=price

if min_price!=10**5:
	print(min_price)
else:
	print(-1)





