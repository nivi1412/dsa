#graph_minhttrees.py
import ast


n=int(input("enter the node count: "))
edges=input("enter the edge list")
edges=ast.literal_eval(edges)

#build adjacensy list and find degree
graph={}
degree={}
trim={}

for edge in edges:
	if edge[0] not in graph:
		graph[edge[0]]=[]
		degree[edge[0]]=0
		trim[edge[0]]=False
	if edge[1] not in graph:
		graph[edge[1]]=[]
		degree[edge[1]]=0
		trim[edge[1]]=False
	graph[edge[0]].append(edge[1])
	graph[edge[1]].append(edge[0])
	degree[edge[0]]+=1
	degree[edge[1]]+=1

print(degree)
print(graph)

for key,value in degree.items():
	if value==1:
		trim[key]=True
		for val in graph[key]:
			degree[value]-=1
print(degree)
print(trim)


#now update graph by trimming the leaf nodes
#node with degree 1 is leaf node

# for node in degree:



