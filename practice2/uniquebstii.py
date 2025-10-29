#uniquebstii.py

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
		print("root.right:",root.right)
		print("right",root.right.data)
	print_binarytree(root.left)
	print_binarytree(root.right)

def uniquebstii(start,end,dp):
	if (start,end) in dp:
		return dp[(start,end)]
	if start>end:
		return [None]
	elif start==end:
		return [node(start+1)]
	else:
		finallist=[]
		for i in range(start,end+1):
			left=uniquebstii(start,i-1,dp)
			right=uniquebstii(i+1,end,dp)
			for l in left:
				for r in right:
					root=node(i+1)
					root.left=l
					root.right=r
					finallist.append(root)
		dp[(start,end)]=finallist
	return dp[(start,end)]



n=int(input("enter the node count:"))

dp={}
start=0
end=n-1
for i in uniquebstii(start,end,dp):
	print_binarytree(i)

