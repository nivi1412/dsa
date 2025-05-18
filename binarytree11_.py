from binarytree_lib import build_binarytree

def binary_tree_paths(root):
	if root.left == None and root.right == None:
		return [str(root.data)]
	lists=[]
	if root.left != None:
		left_list=binary_tree_paths(root.left)
		for l in left_list:
			print("l:",l)
			lists.append(l)
	if root.right != None:
		right_list=binary_tree_paths(root.right)
		for l in right_list:
			print("r:",l)
			lists.append(l)
	for i in range(len(lists)):
		lists[i]=str(root.data)+"->"+lists[i]
	return lists

inp=input("enter the nodes of the binary tree seprated by spaces")
inp=inp.split()
root=build_binarytree(inp)
lists = binary_tree_paths(root)
print(lists)