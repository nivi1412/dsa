#graph24.py
# Loud and Rich
import ast

def DFS(finaldict,node,quiet,memo):
	if node in memo:
		return memo[node]
	min_val=(quiet[node],node)
	key=(node,quiet[node])
	for next_node in finaldict[key]:
		val=DFS(finaldict,next_node,quiet,memo)
		if val < min_val:
			min_val=val
	memo[node]=min_val
	return min_val

inp=input("enter the richer array:")
inp=ast.literal_eval(inp)
quiet=input("enter quiet array:")
quiet=ast.literal_eval(quiet)

richer={}
finaldict={}
result=[]
memo={}
for rich in inp:
	if rich[1] not in richer:
		richer[rich[1]]=[]
	if rich[0] not in richer:
		richer[rich[0]]=[]
	richer[rich[1]].append(rich[0])

sorted_nodes = sorted(richer.keys())
for key in sorted_nodes:
	finaldict[(key,quiet[key])]=richer[key]
print(finaldict)

min_val=next(iter(finaldict))[1]
for cur_node in finaldict:
	node=cur_node[0]
	min_val=(cur_node[1],node)
	value=DFS(finaldict,node,quiet,memo)
	result.append(value[1])
print(result)









