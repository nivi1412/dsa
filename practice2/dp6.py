# dp6.py
#uniquebst

class node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def print_binarytree(root):
	if root==None:
		return
	print(root.data)
	if root.left!=None:
		print("left:",root.left.data)
	if root.right!=None:
		print("root.right:",root.right.data)
		print("right",root.right.data)
	print_binarytree(root.left)
	print_binarytree(root.right)

def unique_BST(start,end,dp):

	if (start,end) in dp:
		return dp[(start,end)]
	if start>end:
		return [None]
	if start==end:
		return [node(start+1)]
	if start<end:
		finallist=[]
		for i in range(start,end+1):
			left=unique_BST(start,i-1,dp)
			right=unique_BST(i+1,end,dp)
			for l in left:
				for r in right:
					root=node(i+1)
					root.left=l
					root.right=r
					finallist.append(root)
		dp[(start,end)]=finallist
	return dp[(start,end)]

n=int(input("enter the node count: "))
my_list=[i+1 for i in range(n)]
start=0
end=n-1
dp={}
for i in (unique_BST(start,end,dp)):
	print_binarytree(i)
	print("------------")