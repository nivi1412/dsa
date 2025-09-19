#graph_town_judge.py
import ast

n=int(input("enter the people count: "))
trust=input("input the edges for the graph: ")

trust=ast.literal_eval(trust)
graph={}
outward_degree={}
inward_degree={}

is_key_found=-1

for i in range(1,n+1):
	graph[i]=[]
	inward_degree[i]=0
	outward_degree[i]=0

for edge in trust:
	graph[edge[0]].append(edge[1])
	outward_degree[edge[0]]+=1
	inward_degree[edge[1]]+=1

print(graph)
print("od:",outward_degree)
print("id:",inward_degree)

for key in graph:
	if not graph[key]:
		if outward_degree[key]==0 and inward_degree[key]==n-1:
			is_key_found=key
print(is_key_found)
