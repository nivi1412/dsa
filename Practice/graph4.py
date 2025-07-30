#graph4.py

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

import ast

trust=input("enter the array trust:")
trust=ast.literal_eval(trust)
trust_dict={}
visited={}
town_judge={}
count=0

for i in range(len(trust)):
	visited[trust[i][0]]=False
	visited[trust[i][1]]=False
	town_judge[trust[i][0]]=False
	town_judge[trust[i][1]]=False
	

for i in range(len(trust)):

	if visited[trust[i][0]]==False:
		town_judge[trust[i][1]]=True
		visited[trust[i][0]]=True
		trust_dict[trust[i][0]]=[]
		trust_dict[trust[i][0]].append(trust[i][1])
	else:
		# print(i,trust_dict[i][0])
		trust_dict[trust[i][0]].append(trust[i][1])
print(visited)
print(town_judge)
for key,value in town_judge.items():
	if value==True:
		data=key
		count+=1
if count==1:
	print("town judge is:",data)
else:
	print(-1)
