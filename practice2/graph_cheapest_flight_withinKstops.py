# graph_cheapest_flight_withinKstops.py
import ast
import heapq


n=int(input("enter the stop count:"))
flights=input("enter the flight details: ")
flights=ast.literal_eval(flights)

src=int(input("enter the source: "))
dst=int(input("enter the destination: "))
k=int(input("enter the stop count: "))
is_dst_reached=False


graph={}
# visited={}
degree={}
heap=[]

for i in range(n):
	graph[i]={}
	# visited[i]=False
	degree[i]=0

for flight in flights:
	graph[flight[0]][flight[1]]=flight[2]
	degree[flight[0]]+=1
	degree[flight[1]]+=1

print(graph)
# print(visited)
print(degree)

# degree[src]-=1
heapq.heappush(heap,(0,src,k+1))

while heap:
	dist,next_src,stopcount=heapq.heappop(heap)
	# print(dist,next_src,stopcount)
	if stopcount==0:
		if next_src==dst:
			print(dist)
			is_dst_reached=True
			break
	else:
		stopcount-=1
		for next_dst,next_dist in graph[next_src].items():
			# print("----",next_dst,next_dist)
			heapq.heappush(heap,(dist+next_dist,next_dst,stopcount))

if not is_dst_reached:
	print(-1)

























