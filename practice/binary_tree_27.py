#binarytree27.py
#129. Sum Root to Leaf Numbers

# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

from binarytree1 import build_binarytree,print_binarytree
def sumrootleafnums(root):
	result=[]
	if root == None:
		return []
	else:
		if root.left ==None and root.right ==None:
			return [[root.data]]
		left=sumrootleafnums(root.left)
		right=sumrootleafnums(root.right)

		for i in left:
			i[0]=root.data+i[0]
			result.append(i)
		for k in right:
			k[0]=root.data+k[0]
			result.append(k)
		return result

Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
my_list=sumrootleafnums(root)
Sum=0
for i in my_list:
	Sum=Sum+int(i[0])
print(Sum)
