# graph_cheapest_flight_withinKstops.py
import ast

def DFS(graph,node,k,dst,weight):
	if node==dst:
		return weight
	else:
		for next_node,val in graph[node].items():
			if k==0:
				if next_node==dst:
					return weight
				return -1
			if degree[next_node]:
				degree[next_node]-=1
				k-=1
				weight+=val
				return DFS(graph,next_node,k,dst,weight)

n=int(input("enter the stop count:"))
flights=input("enter the flight details: ")
flights=ast.literal_eval(flights)

src=int(input("enter the source: "))
dst=int(input("enter the destination: "))
k=int(input("enter the stop count: "))


graph={}
visited={}
degree={}

for i in range(n):
	graph[i]={}
	visited[i]=False
	degree[i]=0

for flight in flights:
	print(flight)
	graph[flight[0]][flight[1]]=flight[2]
	degree[flight[0]]+=1
	degree[flight[1]]+=1

print(graph)
print(visited)
print(degree)

degree[src]-=1
print(DFS(graph,src,k+1,dst,0))

