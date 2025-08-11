#graph24.py
# Loud and Rich
import ast

def DFS(finaldict,node,quiet,min_val,memo):
	if node in memo:
		print("node,memo[node]:",node,memo[node])
		return memo[node]
	if quiet[node]<min_val:
		min_val=quiet[node]
	key=(node,quiet[node])
	for next_node in finaldict[key]:
		print(next_node)
		min_val=DFS(finaldict,next_node,quiet,int(min_val),memo)
		memo[node]=quiet.index(min_val)
	return min_val
		
inp=input("enter the richer array:")
inp=ast.literal_eval(inp)
quiet=input("enter quiet array:")
quiet=ast.literal_eval(quiet)

richer={}
finaldict={}
memo={}
result=[]
for rich in inp:
	if rich[1] not in richer:
		richer[rich[1]]=[]
	if rich[0] not in richer:
		richer[rich[0]]=[]
	richer[rich[1]].append(rich[0])

for key in richer:
	finaldict[(key,quiet[key])]=richer[key]
print(finaldict)

min_val=next(iter(finaldict))[1]
for cur_node in finaldict:
	node=cur_node[0]
	min_val=cur_node[1]
	value=DFS(finaldict,node,quiet,min_val,memo)
	result.append(quiet.index(value))
print(result)









