#graph_cousescheduleII_BFS.py
import ast
from collections import deque

numcourses=int(input("enter no of courses: "))
prerequisites=input("enter the prerequisites: ")
prerequisites=ast.literal_eval(prerequisites)

#topologicalsort

#1.find the inward degree
inward_degree={}
graph={}
q=deque()
my_list=[]

for i in range(numcourses):
	inward_degree[i]=0
	graph[i]=[]
print(graph)
print(inward_degree)
for edge in prerequisites:
	graph[edge[1]].append(edge[0])
	inward_degree[edge[0]]+=1

for key,values in inward_degree.items():
	if values==0:
		q.append(key)

while q:
	value=q.popleft()
	my_list.append(value)
	for next_val in graph[value]:
		inward_degree[next_val]-=1
		if inward_degree[next_val]==0:
			q.append(next_val)

print(my_list)

