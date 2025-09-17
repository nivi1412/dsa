#binarytree.py
#pathsum_returns --- #pathsum retun all paths of binary tree whose sum is equal to target sum

from binarytree1 import build_binarytree,print_binarytree

def pathsum(root,targetsum):

	if root==None:
		return []
	targetsum=targetsum-int(root.data)
	if root.left==None and root.right==None and targetsum==0:
		return [[root.data]]

	left=pathsum(root.left,targetsum)
	right=pathsum(root.right,targetsum)

	result=[]
	for i in left:
		i.insert(0,root.data)
		result.append(i)
	for j in right:
		j.insert(0,root.data)
		result.append(j)

	return result



Arr=input("enter elements of binarytree")
Arr=Arr.split()

targetsum=int(input("enter the target sum:"))
root=build_binarytree(Arr)
result=pathsum(root,targetsum)
print(result)




