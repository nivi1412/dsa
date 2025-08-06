#graph13.py
#Evaluate Division
import ast

def evaluate_division(start_node,end_node,adjacency_dict,edge_weight,muliplication_weight,visited):
	result=[]
	if start_node not in adjacency_dict:
		return -1.00000
	if start_node==end_node:
		return muliplication_weight
	visited[start_node]=True
	original_weight = muliplication_weight
	for next_node in adjacency_dict[start_node]:
		if visited[next_node]==False:
			visited[next_node]=True
			if next_node==end_node:
				muliplication_weight=original_weight*edge_weight[start_node][end_node]
				return muliplication_weight
			muliplication_weight = original_weight * edge_weight[start_node][next_node]
			print("multiply:",muliplication_weight)
			result.append(evaluate_division(next_node,end_node,adjacency_dict,edge_weight,muliplication_weight,visited))
			print("result:",result)
	for i in result:
		if i>0:
			return i
	return -1.00000

equations=input("enter the values seperated by spaces: ")
equations=ast.literal_eval(equations)
values=input("enter the edge weights: ")
values=ast.literal_eval(values)
queries=input("enter the queries: ")
queries=ast.literal_eval(queries)


adjacency_dict={}
edge_weight={}
visited={}
for i in range(len(equations)):
	if equations[i][0] not in adjacency_dict:
		adjacency_dict[equations[i][0]]=[]
		edge_weight[equations[i][0]]={}
		visited[equations[i][0]]=False
	if equations[i][1] not in adjacency_dict:
		adjacency_dict[equations[i][1]]=[]
		edge_weight[equations[i][1]]={}
		visited[equations[i][1]]=False
	adjacency_dict[equations[i][0]].append(equations[i][1])
	adjacency_dict[equations[i][1]].append(equations[i][0])
	edge_weight[equations[i][0]][equations[i][1]]=values[i]
	edge_weight[equations[i][1]][equations[i][0]]=round((1/values[i]),5)

visited_copy=visited.copy()
print(adjacency_dict)
print(edge_weight)
output=[]
for query in queries:
	visited=visited_copy.copy()
	start_node=query[0]
	end_node=query[1]
	muliplication_weight=1
	output.append(evaluate_division(start_node,end_node,adjacency_dict,edge_weight,muliplication_weight,visited))
print(output)

