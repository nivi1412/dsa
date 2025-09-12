# graph_parallelcousesIII.py
import ast

relations=input("enter the relations: ")
relations=ast.literal_eval(relations)
time=input("enter the time:")
time=ast.literal_eval(time)

graph={}

for my_list in relations:
	if my_list[0] not in relations:
		graph[my_list[0]]=[]
	if my_list[1] not in relations:
		graph[my_list[1]]=[]

	relations[my_list[0]].append(my_list[1])



