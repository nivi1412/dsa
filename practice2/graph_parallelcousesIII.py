# graph_parallelcousesIII.py

#1.value in next level having common child node is repeatedly appending 
#2.for graph like this [[1,5],[2,5],[3,5],[3,4],[4,5]] it will give wrong answer as 4,5 both at a time considered at 1,2 levels 2,3 level respecively


import ast
from collections import deque

relations=input("enter the relations: ")
relations=ast.literal_eval(relations)
time=input("enter the time:")
time=ast.literal_eval(time)

graph={}

for my_list in relations:
	if my_list[0] not in graph:
		graph[my_list[0]]=[]

	graph[my_list[0]].append(my_list[1])

print(graph)
print(graph[1])

q=deque()
for key in graph:
	q.append([key,1])
prev_level=1
time_taken=-10000
total_time=0

while q:
	val,level=q.popleft()

	if level==prev_level:
		time_taken=max(time[val-1],time_taken)
	else:
		total_time+=time_taken
		time_taken=max(-10000,time[val-1])
	print("time_taken,total_time,level:",time_taken,total_time,level)

	for value in graph.get(val,[]):
		q.append([value,level+1])

	prev_level=level

print("total time:",total_time+time_taken)

