#reconstruct_itinerary.py
#{'JFK': {'ATL': 1, 'SFO': 1}, 'SFO': {'ATL': 1}, 'ATL': {'JFK': 1, 'SFO': 1}}
import ast

def reconstruct_itinerary(graph,itinerary,start):
	itinerary.append(start)
	for next_node in graph[start]:
		if graph[start][next_node]:
			graph[start][next_node]-=1
			reconstruct_itinerary(graph,itinerary,next_node)


tickets=input("enter the tickets list: ")
tickets=ast.literal_eval(tickets)

graph={}
degree={}
itinerary=[]

for ticket in tickets:
	if ticket[0] not in graph:
		graph[ticket[0]]={}
	if ticket[1] not in graph:
		graph[ticket[1]]={}
	if ticket[1] not in graph[ticket[0]]:
		graph[ticket[0]][ticket[1]]=1
	else:
		graph[ticket[0]][ticket[1]]+=1

for key,values in graph.items():
	graph[key]={k: values[k] for k in sorted(values)}

reconstruct_itinerary(graph,itinerary,'JFK')

print(itinerary)