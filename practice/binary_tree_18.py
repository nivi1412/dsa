#binarytree18.py
#pathsum is equal to target sum
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true

from binarytree1 import build_binarytree,print_binarytree

def pathsum(root,targetsum):
	if root:
		targetsum=targetsum-int(root.data)
		print(root.data,targetsum)
		return pathsum(root.left,targetsum) or pathsum(root.right,targetsum)

	else:
		if targetsum!=0:
			return False
		else: 
			return True




Arr=input("enter elements of binarytree")
Arr=Arr.split()
targetsum=int(input("enter the target sum:"))

root=build_binarytree(Arr)
print(pathsum(root,targetsum))
