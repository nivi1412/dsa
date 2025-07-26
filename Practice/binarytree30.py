#binarytree30.py
#865. Smallest Subtree with all the Deepest Nodes

#Step1. find path with depth

from binarytree1 import build_binarytree,print_binarytree

def findtreepathwithdepth(root):
	if root==None:
		return []
	else:
		result=[]
		if root.left==None and root.right==None:
			return [[root.data,1]]
		left=findtreepathwithdepth(root.left)
		right=findtreepathwithdepth(root.right)
		for i in left:
			i.insert(0,root.data)
			i[-1]=i[-1]+1
			result.append(i)
		for j in right:
			j.insert(0,root.data)
			j[-1]=j[-1]+1
			result.append(j)
		return result

def findnode(root,target_node):
	if root==None:
		return
	if root.data==target_node:
		return root
	else:
		left=findnode(root.left,target_node)
		right=findnode(root.right,target_node)
		
		if left!=None and right ==None:
			return left
		elif left==None and right !=None:
			return right


Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
result=findtreepathwithdepth(root)
print(result)
my_list=[]
Max=result[0][-1]
for i in result:
	if Max<i[-1]:
		Max=i[-1]
print(Max)
for i in result:
	if i[-1]==Max:
		my_list.append(i)
if len(my_list)>1:
	for i in range(len(my_list[0])-1):
		value=my_list[0][i]
		for j in range(1,len(my_list),+1):
			if my_list[j][i]!=value:
				target_node=my_list[0][i-1]
				break
else:
	target_node=my_list[0][-2]
print(target_node)
print_binarytree(findnode(root,target_node))








