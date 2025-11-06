#network_delay.py
import ast
import math

def network_delay(node,graph,weight):
	val=weight
	for next_node,next_weight in graph[node].items():
		val=max(val,network_delay(next_node,graph,weight+next_weight))
		print("val:",val)

	return val

times=input("enter the times: ")
times=ast.literal_eval(times)
k=int(input("enter the strat node: "))

graph={}

for time in times:
	if time[0] not in graph:
		graph[time[0]]={}
	if time[1] not in graph:
		graph[time[1]]={}
	graph[time[0]][time[1]]=time[2]

print(graph)
min_time=-1

for node,weight in graph[k].items():
	min_time=max(min_time,network_delay(node,graph,weight))

print(min_time)