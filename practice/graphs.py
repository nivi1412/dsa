#Graphs.py
from collections import deque

edges=input("enter the edges to construct the graph:")
edges=edges.split()
visited={}
my_dict={}
for i in range(0,len(edges),+2):
	if edges[i] in my_dict:
		my_dict[edges[i]].append(edges[i+1])
	else:
		my_dict[edges[i]]=[]
		my_dict[edges[i]].append(edges[i+1])
	visited[edges[i]]=False
	visited[edges[i+1]]=False
print(my_dict)
start_node=input("enter the start_node:")
end_node=input("enter the end node:")
q=deque()
level=0
for i in my_dict:
	visited[i]=False
print(visited)
q.append([start_node,level])
visited[start_node]=True
while q:
	value,level=q.popleft()
	print("value:",value)
	if value==end_node:
		print("distance:",level)
		break
	for i in my_dict[value]:
		if visited[i]==False:
			q.append([i,level+1])
			visited[i]=True





