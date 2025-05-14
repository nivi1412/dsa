#dict1.py
# Input
# ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
# [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
# Output
# [null, null, null, 5, 10, null, 5, null, 2]

# Rahul => Update max and min logic to O(1)
# initialize curr_max=None and while updating make logic if currmax is none them current value to logic 

import ast
from collections import OrderedDict


def StockPrice(inp,dic):
	od=OrderedDict()
	out=[]
	for command,lists in zip(inp,dic):

		if command == "update":
			od[lists[0]]=lists[1]
			out.append("null")
			
		elif command == "current":
			last_entry=next(reversed(od))
			out.append(od[last_entry])

		elif command == "maximum":
			out.append(max(od.values()))

		elif command == "update":
			for key,value in od:
				if key==lists[0]:
					od[key]=lists[1]

		elif command == "minimum":
			out.append(min(od.values()))

		else:
			out.append("null")

	return out



inp=input("enter the commands:")
dic=input("enter the stockprices at timestamps:")

inp=ast.literal_eval(inp)
dic=ast.literal_eval(dic)

print(inp)
print(dic)

for command in inp:
	if command == 'StockPrice':
		out=StockPrice(inp,dic)
print(out)
