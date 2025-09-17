#graph_depth.py
from collections import deque

Arr=input("enter the array edges:")
Arr=list(map(int,Arr.split()))
source=int(input("enter the source node:"))
destination=int(input("enter the destination node:"))

graph={}
q=deque()
valied={}
is_destination_reached=False


for i in range(0,len(Arr),2):
	u=Arr[i]
	v=Arr[i+1]
	if u not in graph:
		graph[u]=[]
	if v not in graph:
		graph[v]=[]
	graph[u].append(v)
	graph[v].append(u)
	valied[u]=True
	valied[v]=True

for nodes in graph:
	print(f"{nodes}:{graph[nodes]}")

position=0
q.append([source,position])
while q:
	[var,position]=q.popleft()
	if var==destination:
		print("destination reached and depth is:",position)
		is_destination_reached=True
		break
	if valied[var]==True:
		for node in graph[var]:
			q.append([node,position+1])
	valied[var]=False

if not is_destination_reached:
	print("not possible")




