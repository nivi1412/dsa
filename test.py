from collections import dict

A=input("enter the edges:")
A=A.split(",")
local=[]
my_list=[]
my_dict={}
prev=10*5
for i in A:
	local.append(i.split(" "))
for i in local:
	if i[0]!=prev:
		my_list.append(i[1])
		


