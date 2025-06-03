#recoverBST.py
# def recoverBST(my_list):
# 	prev=my_list[0]
# 	count=0
# 	for i in range(1,len(my_list),+1):
# 		curr=my_list[i]
# 		if prev > curr and count==0:
# 			swap1=prev
# 			count=1
# 		elif prev > curr and count==1:
# 			swap2=curr

from binarytree_practice1 import build_binarytree,print_binarytree

def recoverBST(my_list,isadjacent):
	if isadjacent:
		prev=my_list[0]
		for i in range(len(my_list)):
			if prev>my_list[i]:
				local=prev
				prev=my_list[i]
				my_list[i]=local
	else:
		




def isadjacent(my_list):
	prev=my_list[0]
	count=0
	for i in my_list:
		if prev > i:
			count+=1
		prev=i
	if count==1:
		isadjacent=True
	else: isadjacent=False
	recoverBST(my_list,isadjacent)


def inordertraversal(root):
	if root.left!=None:
		inordertraversal(root.left,my_list)
	if root!=None:
		my_list.append(root.data)
	if root.right!=None:
		inordertraversal(root.right,my_list)
	isadjacent(my_list)



inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
my_list=[]
inordertraversal(root,my_list)