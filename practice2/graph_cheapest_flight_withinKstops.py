# graph_cheapest_flight_withinKstops.py
import ast

def DFS(graph,node,k,weight):



n=int(input("enter the stop count:"))
flights=input("enter the flight details: ")
flights=ast.literal_eval(flights)

src=int(input("enter the source: "))
dst=int(input("enter the destination: "))
k=int(input("enter the stop count: "))


graph={}
visited={}


for i in range(n):
	graph[i]={}
	visited[i]=False

for flight in flights:
	print(flight)
	graph[flight[0]][flight[1]]=flight[2]

print(graph)
print(visited)

DFS(graph,next(iter(graph)),k,0)

