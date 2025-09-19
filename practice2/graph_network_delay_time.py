#graph_network_delay_time.py
import ast
def network_delaytime(node,graph,time,visited):
	for next_node,next_time in graph[node].items():
		if visited[next_node]==False:
			visited[next_node]=True
			time=time+network_delaytime(next_node,graph,next_time,visited)
			print("time:",node,next_node,time)
	return time

times=input("enter the list of traveltimes: ")
times=ast.literal_eval(times)
k=int(input("enter the start node: "))

graph={}
visited={}

for values in times:
	if values[0] not in graph:
		graph[values[0]]={}
		visited[values[0]]=False
	if values[1] not in graph:
		graph[values[1]]={}
		visited[values[1]]=False

	graph[values[0]][values[1]]=values[2]

out=-1
print(graph)
visited[k]=True
for next_node,time in graph[k].items():
	if visited[next_node]==False:
		visited[next_node]=True
		print("next_node",next_node)
		out=max(out,network_delaytime(next_node,graph,time,visited))
	
print(out)



