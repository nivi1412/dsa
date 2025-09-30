#graph_dikjstaw.py

import ast
import heapq

inp=input("enter the places and corresponding distqances: ")
src=input("enter the source:")
roadmap=ast.literal_eval(inp)

heap=[]
visited_loc= {}
graph={}
final_out={}
final_out[src]={}



for road in roadmap:
	if road[0] not in graph:
		graph[road[0]]=[]
		visited_loc[road[0]]=False
	if road[1] not in graph:
		graph[road[1]]=[]
		visited_loc[road[1]]=False
	graph[road[0]].append([road[1],road[2]])

print(graph)
heapq.heappush(heap,(0,next(iter(graph))))
visited_loc[next(iter(graph))]=True

while heap:
	cur_dist,cur_src=heapq.heappop(heap)
	final_out[src][cur_src]=cur_dist
	for next_src in graph[cur_src]:
		if visited_loc[next_src[0]]==False:
			visited_loc[next_src[0]]=True
			heapq.heappush(heap,(next_src[1]+cur_dist,next_src[0]))

print(final_out)




