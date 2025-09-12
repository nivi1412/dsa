# Graph_reconstruct_itenerary.py(data structure, dict(dict))
import ast

def reconstruct_itinerary(sorted_graph,my_list,node):
	my_list.append(node)

	for next_node,values in sorted_graph[node].items():
		print(next_node)
		if values:
			sorted_graph[node][next_node]-=1
			reconstruct_itinerary(sorted_graph,my_list,next_node)

tickets=input("enter the tickets: ")
tickets=ast.literal_eval(tickets)

graph={}

for route in tickets:
	if route[0] not in graph:
		graph[route[0]]={}
	if route[1] not in graph:
		graph[route[1]]={}
	if route[1] not in graph[route[0]]:
		graph[route[0]][route[1]]=1
	else:
		graph[route[0]][route[1]]+=1

print(graph)

sorted_graph={k: {city:v[city] for city in sorted(v)} for k,v in graph.items()}
my_list=[]
print(sorted_graph)
reconstruct_itinerary(sorted_graph,my_list,"JFK")
print(my_list)

