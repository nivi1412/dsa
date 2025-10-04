# graph_alien_dictionary.py

# A new alien language uses the English alphabet, but the order of the letters is unknown. You are given a list of words from the dictionary, 
# sorted lexicographically by the rules of this alien language.

# Write a function to derive the order of letters in this alien language.

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"

import ast

def DFS(start_node,graph,result):
	print(result)
	if not graph[start_node]:
		return start_node
	else:
		for next_node in graph[start_node]:
			result=result+DFS(next_node,graph,next_node)
		return result


words=input("enter the words list: ")
words=ast.literal_eval(words)
my_list=[]

for i in range(len(words)-1):
	len1=len(words[i])
	len2=len(words[i+1])
	length=min(len1,len2)
	j=0
	print(words[i],words[i+1])
	while(j<length):
		if words[i][j]!=words[i+1][j]:
			my_list.append([words[i][j],words[i+1][j]])
			break
		j+=1
print(my_list)
graph={}
indegree={}
is_cycle=False

if my_list:
	for l in my_list:
		if l[0] not in indegree:
			graph[l[0]]=[]
			indegree[l[0]]=0
		if l[1] not in indegree:
			graph[l[1]]=[]
			indegree[l[1]]=0
		graph[l[0]].append(l[1])
		indegree[l[1]]+=1
	print(graph)
	print(indegree)

	for letter in indegree:
		if indegree[letter]==0:
			start_node=letter
		else:
			is_cycle=True

	# result=start_node
	if not is_cycle:
		result=DFS(start_node,graph,start_node)
	else:
		result=""

	print(result)
else:
	print("")




