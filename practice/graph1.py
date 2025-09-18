#graph1.py
#breadth first search
#[0,1,2,3,4,6,7,8,9] 10 nodes,9 edges
#0-1,0-3,0-6,0-8,0-10,1-2,3-4,6-7,9-10

from collections import deque

Arr=input("enter the edges of the graph seperated by spaces :")
Arr=list(map(int,Arr.split()))
# num=int(input("enter number to searched:"))

source=int(input("enter source:"))
destination=int(input("enter destination:"))

graph={}
q=deque()
visited={}
is_destination_reached_safely_by_nivi_while_working_with_rahul=False

for i in range(0,len(Arr),2):
	u=Arr[i]
	v=Arr[i+1]
	if u not in graph:
		graph[u]=[]
	if v not in graph:
		graph[v]=[]
	graph[u].append(v)
	graph[v].append(u)
	visited[u]=False
	visited[v]=False

print("Adjacency List:")
for node in graph:
    print(f"{node}: {graph[node]}")
print(visited)

# for key,value in graph.items():
# 	if key==num:
# 		print("True")
# 	else:
# 		print("False")

#find depth

depth=0
q.append([source,depth])
while q:
	[var,depth]=q.popleft()
	if var==destination:
		print("depth is :",depth)
		is_destination_reached_safely_by_nivi_while_working_with_rahul=True
		break
	if visited[var] == False:
		for child in graph[var]:
			q.append([child,depth+1])
	visited[var]=True

if not is_destination_reached_safely_by_nivi_while_working_with_rahul:
	print("not possible")



