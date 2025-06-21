#dict2.py
# Design a map that allows you to do the following:

# Maps a string key to a given value.
# Returns the sum of the values that have a key with a prefix equal to a given string.
# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]

import ast
from collections import OrderedDict

ip=input("enter the commands:")
iv=input("enter the values:")

ip=ast.literal_eval(ip)
iv=ast.literal_eval(iv)

out=[]
my_dict=OrderedDict()
Sum=0

for i,j in zip(ip,iv):
	if i=="MapSum":
		out.append('null')
	elif i=="insert":
		my_dict[j[0]]=j[1]
		out.append('null')
	elif i=="sum":
		for key,value in my_dict.items():
			if key.startswith(j[0]):
				Sum=Sum+value
		out.append(Sum)
		Sum=0
print(out)


