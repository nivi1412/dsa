#graph24.py
# Loud and Rich
import ast

def DFS(richer,node,quiet,memo):
	if node in memo:
		return memo[node]
	min_pair = (quiet[node], node)
	for next_node in richer[node]:
		child_min_pair=DFS(richer,next_node,quiet,memo)
		if child_min_pair[0] < min_pair[0]:
			min_pair = child_min_pair
	memo[node]=min_pair
	return memo[node]

inp=input("enter the richer array:")
inp=ast.literal_eval(inp)
quiet=input("enter quiet array:")
quiet=ast.literal_eval(quiet)

richer={}
memo={}
result=[]
for rich in inp:
	if rich[1] not in richer:
		richer[rich[1]]=[]
	if rich[0] not in richer:
		richer[rich[0]]=[]
	richer[rich[1]].append(rich[0])

print(richer)

sorted_nodes = sorted(richer.keys())
for node in sorted_nodes:
	value=DFS(richer,node,quiet,memo)
	result.append(value[1])
print(result)









