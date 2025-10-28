# Course_scheduleii.py
import ast

def course_schedule(node,inward_degree,graph,finallist):
	if node not in finallist and inward_degree[node]==0:
		finallist.append(node)
	for next_node in graph[node]:
		inward_degree[next_node]-=1
		if inward_degree[next_node]==0:
			course_schedule(next_node,inward_degree,graph,finallist)


numcourses=int(input("enter the course count: "))
prerequisites=input("enter the prerequisites: ")
prerequisites=ast.literal_eval(prerequisites)

graph={}
visited={}
finished={}
inward_degree={}

for i in range(numcourses):
	graph[i]=[]
	inward_degree[i]=0

for course in prerequisites:
	graph[course[1]].append(course[0])
	inward_degree[course[0]]+=1

print(graph)
print(inward_degree)

degree=[]
finallist=[]

for node,value in inward_degree.items():
	if value==0:
		degree.append(node)
		finallist.append(node)

if len(degree)!=0:
	for start_node in degree:
		course_schedule(start_node,inward_degree,graph,finallist)

print(finallist)

