#graph12.py
#reconstruct itenerary
import ast

def reconstruct_itinerary(start_city,graph,itinerary):
	itinerary.append(start_city)
	print(start_city)

	if len(graph[start_city]):
		next_city=next(iter(graph[start_city]))
		graph[start_city][next_city] -= 1
		if graph[start_city][next_city] == 0:
			del graph[start_city][next_city]
		reconstruct_itinerary(next_city, graph, itinerary)
	return itinerary


tickets=input("enter the tickets [from,to]: ")
tickets=ast.literal_eval(tickets)
graph={}
for city in tickets:
	if city[0] not in graph:
		graph[city[0]]={}
	if city[1] not in graph:
		graph[city[1]]={}
	if city[1] in graph[city[0]]:
		graph[city[0]][city[1]] += 1
	else:
		graph[city[0]][city[1]] = 1

print(graph)

for key, value in graph.items():
	graph[key] = {k: value[k] for k in sorted(value.keys())}

print(graph)

print("itinerary with cycle: ",reconstruct_itinerary("JFK",graph,[]))


