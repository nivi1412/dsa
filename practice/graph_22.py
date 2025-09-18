#graph22.py
#Find Eventual Safe States
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]

import ast
import heapq

def detect_cycle(graph,node,visited,finished,memo):
	cycle=False
	visited[node]=True
	if node in memo and memo[node]==True:
		return True
	for next_node in graph[node]:
		print(next_node)
		if finished[next_node]==False and visited[next_node]==True:
			return True
		if visited[next_node]==False:
			visited[next_node]=True
			cycle=cycle or detect_cycle(graph,next_node,visited,finished,memo)
			# return cycle
	memo[node]=cycle
	finished[node]=True
	return cycle

inp=input("enter the graph: ")
inp=ast.literal_eval(inp)

graph={}
visited={}
finished={}
memo={}
final_list=[]
safe=False

for i in range(len(inp)):
	if inp[i] == []:
		visited[i]=False
		finished[i]=False
	graph[i]=inp[i]
	visited[i]=False
	finished[i]=False
visited_copy=visited.copy()
finished_copy=finished.copy()

#detect cycle from each node return node is safe or not
for node in graph:
	visited=visited_copy.copy()
	finished=finished_copy.copy()
	cycle=detect_cycle(graph,node,visited,finished,memo)
	if not cycle:
		heapq.heappush(final_list,node)
print(final_list)
