# #dict2.py
# Design a map that allows you to do the following:

# Maps a string key to a given value.
# Returns the sum of the values that have a key with a prefix equal to a given string.
# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]

# Rahul => Solve using trie data structure

import ast
from collections import OrderedDict

class MapSum:
	def __init__(self):
		self.od={}

	def insert(self,key,value):
		self.od[key]=value

	def sum(self,prefix):
		summ=0
		for key,values in self.od.items():
			if key.startswith(prefix):
				summ=summ+values
		return summ

inp=input("enter the commands:")
lis=input("enter the key value pairs:")

commands=ast.literal_eval(inp)
lists=ast.literal_eval(lis)
output=[]
for command,lists in zip(commands,lists):
	if command=="MapSum":
		map_sum=MapSum()
		output.append("null")
	if command == "insert":
		map_sum.insert(lists[0],lists[1])
		output.append("null")
	if command == "sum":
		prefix=lists[0]
		add=map_sum.sum(prefix)
		output.append(add)
print(output)

