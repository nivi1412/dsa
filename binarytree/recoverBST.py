#recoverBST.py

from binarytree_practice1 import build_binarytree,print_binarytree

def recoverBST(my_list):
	prev=my_list[0]
	count=0
	for i in range(1,len(my_list),+1):
		curr=my_list[i]
		if prev > curr and count==0:
			swap1=prev
			count=1
		elif prev > curr and count==1:
			swap2=curr




def inordertraversal(root):
	if root.left!=None:
		inordertraversal(root.left,my_list)
	if root!=None:
		my_list.append(root.data)
	if root.right!=None:
		inordertraversal(root.right,my_list)

	recoverBST(my_list)


inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
my_list=[]
inordertraversal(root,my_list)