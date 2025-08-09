#graph22.py
#Find Eventual Safe States
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]

import ast
import heapq

def detect_cycle(graph,node,visited,finished):
	cycle=False
	visited[node]=True
	for next_node in graph[node]:
		if finished[next_node]==False and visited[next_node]==True:
			return True
		if visited[next_node]==False:
			visited[next_node]=True
			cycle=cycle or detect_cycle(graph,next_node,visited,finished)
			return cycle
	return cycle
	finished[node]=True


# def detect_safenodes(graph,node,visited,final_list,my_list):
# 	def DFS(graph,node,visited,my_list):
# 		for next_node in graph[node]:
# 			if visited[next_node]==False:
# 				visited[next_node]=True
# 				print("next_node,curr node:",node,next_node)
# 				if ((next_node in my_list) and (node not in final_list)):
# 					print("my_list",my_list,next_node)
# 					heapq.heappush(final_list,node)
# 				DFS(graph,next_node,visited,my_list)
# 		return final_list
# 	return DFS(graph,node,visited,my_list)


inp=input("enter the graph: ")
inp=ast.literal_eval(inp)

graph={}
visited={}
finished={}
final_list=[]
safe=False

for i in range(len(inp)):
	if inp[i] == []:
		visited[i]=False
		finished[i]=False
		heapq.heappush(final_list,i)
	graph[i]=inp[i]
	visited[i]=False
	finished[i]=False
print(graph)
print(visited)
visited_copy=visited.copy()
my_list=final_list.copy()

#detect cycle from each node return node is safe or not
for node in graph:
	safe=detect_cycle(graph,node,visited,finished)
	print(node,safe)

# for node in graph:
# 	visited=visited_copy.copy()
# 	visited[node]=True
# 	final_list=detect_safenodes(graph,node,visited,final_list,my_list)

print(final_list)
