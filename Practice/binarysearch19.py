#binarysearch19.py
#pathsum retun all paths of binary tree

# part1:Return all paths of binarytree

from binarytree1 import build_binarytree,print_binarytree

def pathsum(root):
	result=[]
	if root:
		if root.left!=None or root.right!=None:
			left=pathsum(root.left)
			right=pathsum(root.right)
			for i in left:
				i.insert(0,root.data)
				result.append(i)
			for j in right:
				j.insert(0,root.data)
				result.append(j)
			print("l:",left)
			print("r:",right)
			print("d:",root.data)
			return result
		else:
			return [[root.data]]

	else:
		return []

Arr=input("enter elements of binarytree")
Arr=Arr.split()
#targetsum=int(input("enter the target sum:"))
root=build_binarytree(Arr)
#print_binarytree(root)
print(pathsum(root))