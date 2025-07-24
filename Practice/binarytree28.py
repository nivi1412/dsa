#binarytree28.py
#Construct String from Binary Tree

# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the empty parenthesis pairs. And it will be "1(2(4))(3)".

# Input: root = [1,2,3,null,4]
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, except the () after 2 is necessary to indicate the absence of a left child for 2 and the presence of a right child.

from binarytree1 import build_binarytree,print_binarytree

def constructstring(root):
	if root!=None:
		if root.left==None and root.right ==None:
			return "("+root.data+")"
		if root.left!=None and root.right==None:
			left=constructstring(root.left)
			return "("+root.data+left+")"
		if root.left==None and root.right !=None:
			right=constructstring(root.right)
			return "("+root.data+"()"+right+")"
		if root.left!=None and root.right!=None:
			left=constructstring(root.left)
			right=constructstring(root.right)
			return root.data+left+right


Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
string=constructstring(root)
print(string)