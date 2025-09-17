#uniquebinarysearchtrees_1.py

#learnings:
#1. initialize count and store the count and return after considering all cases

def count_binarytrees(my_list):
	if len(my_list)==0 or len(my_list)==1:
		return 1
	else:
		count=0
		for i in range(len(my_list)):
			left=count_binarytrees(my_list[:i])
			right=count_binarytrees(my_list[i+1:])
			print("i",i)
			print("left",left)
			print("right",right)
			count=count+(left*right)
		return count


#make list of input range
inp=int(input("enter number of nodes of binary tree"))
my_list=[]

for i in range(inp):
	my_list.append(i+1)

print(count_binarytrees(my_list))