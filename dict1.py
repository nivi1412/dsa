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
from sortedcontainers import SortedDict


def StockPrice(inp,dic):
	od=OrderedDict()
	sod=SortedDict()
	out=[]
	for command,lists in zip(inp,dic):

		if command == "update":
			print(lists[0])
			if lists[0] in od:
				price=od[lists[0]]
				if price in sod:
					del sod[price]
			od[lists[0]]=lists[1]
			sod[lists[1]]=lists[0]
			out.append("null")
			print(sod)
			
		elif command == "current":
			last_entry=next(reversed(od))
			out.append(od[last_entry])

		elif command == "maximum":
			print (sod)
			out.append(sod.peekitem(-1)[0])

		elif command == "update":
			for key,value in od:
				if key==lists[0]:
					od[key]=lists[1]

		elif command == "minimum":
			out.append(sod.peekitem(0)[0])

		else:
			out.append("null")

	return out


# [[], [1, 10], [2, 10], [], [], [1, 3], [], [4, 2], []]


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
