# graph_min_cost.py
import ast

 #return min fee
def min_cost(node,graph,time,fee,visited)->int:
	# print("time:",time)
	if graph[node][0][0]==None:
		if time>=0:
			return fee
		else:
			return -1
	else:
		for next_node in graph[node]:
			# print("node:",next_node[0],next_node[1],next_node[2])
			# print("fee till now:",fee)
			if visited[next_node[0]]==False:
				visited[next_node[0]]=True
				result=min_cost(next_node[0],graph,time-next_node[1],next_node[2]+fee,visited)
				# print("result:",result)
				fee=max(fee,result) if result!=-1 else -1
		return fee

max_time=int(input("enter the maximum time: "))
edges=input("enter start,endnodes with the distance: ")
edges=ast.literal_eval(edges)
passingfee=input("enter passing fee: ")
passingfee=ast.literal_eval(passingfee)

graph={}
visited={}

for edge,fee in zip(edges,passingfee):
	# print("edge,fee:",edge,fee)
	if edge[0] not in graph:
		graph[edge[0]]=[]
		visited[edge[0]]=False
	if edge[1] not in graph:
		graph[edge[1]]=[]
		visited[edge[1]]=False

	graph[edge[0]].append([edge[1],edge[2],passingfee[edge[1]]])	

for key,values in graph.items():
	if not values:
		graph[key].append([None,None,passingfee[key]])

# print(graph)
node=next(iter(graph))
visited[node]=True
visited_copy=visited.copy()
min_fee=1001
fee=passingfee[node]
for next_node in graph[node]:
	# print("==============")
	# print(next_node)
	visited=visited_copy.copy()
	visited[next_node[0]]=True
	val=min_cost(next_node[0],graph,max_time-next_node[1],fee+next_node[2],visited)
	min_fee=min(min_fee,val) if val!=-1 else -1
print(min_fee)

