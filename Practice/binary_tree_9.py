#binarytree9.py
#recover Binary search tree
#You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake.
#Recover the tree without changing its structure.

# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]

#steps: 1. store values in a list by doing inorder traversel
#2. from the list find out if the swapped values are adjacent or not
#3. if adjacent swap(changes in ascending order at one place) , 
#if not adjacent we find there will be change in two places for ascending order and then swap them
#4. now we have got inorder traversal of correct BST, add nulls where ever present 
#5.from that construct a BST

from binarytree1 import build_binarytree,print_binarytree

class BST:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def inorder_traversal(root,my_list):
	if root.left!=None:
		inorder_traversal(root.left,my_list)
	if root!=None:
		my_list.append(root.data)
	if root.right!=None:
		inorder_traversal(root.right,my_list)

def is_adjacent(my_list):
	prev_node=int(my_list[0])
	count=0
	for curr_node in range(1,len(my_list),1):
		if int(my_list[curr_node])<prev_node:
			count+=1
		prev_node=int(my_list[curr_node])	
	if count==1:
		return True
	else:
		return False

def Swap_nodes(my_list,adjacent):
	if adjacent:
		prev=0
		for i in range(1,len(my_list),1):
			if my_list[prev]>my_list[i]:
				my_list[prev],my_list[i]=my_list[i],my_list[prev]
				print(my_list)
				return
			prev=i
	else:
		prev=0
		count=0
		for i in range(1,len(my_list),1):
			if my_list[prev]>my_list[i]:
				count+=1
				if count==1:
					swap1=i
					print(swap1)
				elif count==2:
					swap2=i
					print(swap2)
					my_list[swap1],my_list[swap2]=my_list[swap2],my_list[swap1]
					print(my_list)
					return
			prev=i

# def Addnulls(my_list,Arr):
# 	finallist=[]
# 	j=0
# 	for i in Arr:
# 		if i=="null":
# 			finallist.append("null")
# 		else:
# 			finallist.append(my_list[j])
# 			j+=1
# 	return finallist

def buildBST(my_list):
	if not(my_list):
		return None

	mid=len(my_list)//2
	root=BST(my_list[mid])
	left=my_list[:mid]
	right=my_list[mid+1:]
	root.left=buildBST(left)
	root.right=buildBST(right)
	return root



Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
my_list=[]
inorder_traversal(root,my_list)
print(my_list)
adjacent=is_adjacent(my_list)
Swap_nodes(my_list,adjacent)
# my_list=Addnulls(my_list,Arr)
# print(my_list)
root=buildBST(my_list)
print_binarytree(root)








