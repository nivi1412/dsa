#graph21.py
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
price=0
found=False

for flight in flights:
	if flight[0] not in route_map:
		route_map[flight[0]]={}
		# visited[flight[0]]=False
	route_map[flight[0]][flight[1]]=flight[2]

heap=[]
heapq.heappush(heap,([0,src,0]))
cheapest_flight={}
while heap:
	price,src_node,stops_count=heapq.heappop(heap)

	if src_node not in cheapest_flight:
		cheapest_flight[src_node]={}
	if stops_count in cheapest_flight[src_node]:
		continue
	cheapest_flight[src_node][stops_count]=price

	for next_node,next_price in route_map.get(src_node,{}).items():
		if stops_count <= k+1:
			heapq.heappush(heap,[price+next_price,next_node,stops_count+1])

min_price=10**5
for node_count,price in cheapest_flight[dst].items():
	if node_count-1 <= k:
		if price<min_price:
			min_price=price

if min_price!=10**5:
	print(min_price)
else:
	print(-1)


