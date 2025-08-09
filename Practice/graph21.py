#graph21.py
# Cheapest Flights Within K Stops
import ast
from collections import deque

n=int(input("no of cities: "))
flights=input("enter the flights array: ")
flights=ast.literal_eval(flights)
src=int(input("enter the source node: "))
dst=int(input("enter the destination node: "))
k=int(input("enter no of atmost stops from source to destination: "))

route_map={}
visited={}
price=0

for flight in flights:
	if flight[0] not in route_map:
		route_map[flight[0]]={}
		visited[flight[0]]=False
	visited[flight[1]]=False
	route_map[flight[0]][flight[1]]=flight[2]
print(route_map)

q=deque()
q.append([src,0,0])
visited[src]=True
i=0
while q:
	print(q)
	src_node,stops_count,prev_price=q.popleft()
	for next_node,price in route_map.get(src_node,{}).items():
		if visited[next_node]==False:
			visited[next_node]=True
			print(next_node,price)
			q.append([next_node,stops_count+1,prev_price+price])





