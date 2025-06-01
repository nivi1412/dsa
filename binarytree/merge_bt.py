#merge_bt.py

def merge_BT(root1,root2):
	if root1!=None and root2 !=None:
		root1.data=root1.data+root2.data
		root1.left=merge_BT(root1.left,root2.left)
		root1.right=merge_BT(root1.right,root2.right)
	if root1.data==None and root2.data !=None:
		root1=root2
	return root1

inp=input("enter the nodes of tree seperated by spaces:")
inp1=input("enter the nodes of subroot:")
inp=inp.split()
inp1=inp1.split()
root1=build_binarytree(inp)
root2=build_binarytree(inp1)
print(merge_BT(root1,root2))