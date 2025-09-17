#graph_again.py
#practice to print the edges and nodes of the graph

Arr=input("enter the array edges:")
Arr=list(map(int,Arr.split()))
print(Arr)
edges={}
for i in range(0,len(Arr),2):
	u=Arr[i]
	v=Arr[i+1]
	if u not in edges:
		edges[u]=[]
	if v not in edges:
		edges[v]=[]

	edges[u].append(v)
	edges[v].append(u)
	print(edges)

for node in edges:
	print(f"{node}:{edges[node]}")


