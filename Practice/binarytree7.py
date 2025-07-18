#binarytree7.py
#find the unique binary search trees with given no of nodes and return the list of trees possible

def build_BSTfromNode(my_list):
	if len(my_list)==0:
		return [["null"]]
	elif len(my_list)==1:
		return [my_list]
	else:
		finallist=[]
		for i in range(len(my_list)):
			root=my_list[i]
			left_list=my_list[:i]
			right_list=my_list[i+1:]
			left=build_BSTfromNode(left_list)
			right=build_BSTfromNode(right_list)
			#print("left:",i,left)
			#print("right:",i,right)
			for i in left:
				for j in right:
					local=[]
					local.append(root)
					for ele in i:
						local.append(ele)
					for ele in j:
						local.append(ele)
					#print("local:",local)
					finallist.append(local)

	print(finallist)
	return finallist


node_count=int(input("enter number of nodes:"))
my_list=[]
for i in range(node_count):
	my_list.append(i+1)
print(build_BSTfromNode(my_list))