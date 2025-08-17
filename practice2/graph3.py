#graph4.py

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

import ast

inp=input("enter the trust array: ")
inp=ast.literal_eval(inp)

graph={}
inward={}
outward={}

for i in inp:
	if i[0] not in graph:
		graph[i[0]]=[]
		inward[i[0]]=0
	if i[1] not in graph:
		graph[i[1]]=[]
		inward[i[1]]=0
	graph[i[0]].append(i[1])

print(graph)
for key,values in graph.items():
	for i in values:
		inward[key]+=1

print(inward)
is_judge=True
result=[]
count=0
for key,values in inward.items():
	if values==0:
		result.append(key)

if len(result)==1:
	for key,values in graph.items():
		if (result[0] in values) or (graph[key]==result[0] and len(graph[key])>0):
			print(-1)
			is_judge=False
			break
	if is_judge: print(result[0])	

else:
	print(-1)



