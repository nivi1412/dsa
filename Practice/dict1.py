#dict1.py
# Input
# ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
# [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
# Output
# [null, null, null, 5, 10, null, 5, null, 2]
import ast
from collections import OrderedDict
from sortedcontainers import SortedDict


ip=input("enter input processess:")
ip=ast.literal_eval(ip)
iv=input("enter input values:")
iv=ast.literal_eval(iv)

print(ip)
print(iv)
current=0
Max=10**(-5)
Min=10**5
flag=0

out=[]
my_dict=OrderedDict()
sort_dict=SortedDict()

for i,j in zip(ip,iv):
	if i=="StockPrice":
		out.append('null')
	if i=="update":
		if j[0] in my_dict:
			key=my_dict[j[0]]
			flag=1
		if flag:
			del sort_dict[key]
			flag=0
		sort_dict[j[1]]=j[0]
		my_dict[j[0]]=j[1]
		current=j[1]
		out.append('null')
	if i=="current":
		out.append(current)
	if i=="maximum":
		out.append(sort_dict.peekitem(-1)[0])
	if i=="minimum":
		out.append(sort_dict.peekitem(0)[0])
	print(sort_dict)
print(out)
