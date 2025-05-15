#dict3.py
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2

# we use depth first search algorithm(DFS)

class treenode():
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right

# def DFS(root):
# 	i=0
# 	while(i<len(root)):


inp=input("enter the input nodes seperated by spaces")
nodes=inp.split()

treenodes = []
for x in nodes:
	treenodes.append(treenode(x))

for i in range(len(nodes)):
	if (treenodes[i].val == "null"):
		continue
	if (2 * i + 1 < len(nodes)) and treenodes[2 * i + 1].val != "null":
		treenodes[i].left = treenodes[2 * i + 1]
	if (2 * i + 2 < len(nodes)) and treenodes[2 * i + 1].val != "null":
		treenodes[i].right = treenodes[2 * i + 2]
print(treenodes)
for x in treenodes:
	if (x.val == "null"):
		continue
	print(x.val)
	if x.left is not None:
		print("LEFT: ", x.left.val)
	if x.right is not None:
		print("RIGHT: ", x.right.val)

root = treenodes[0]
# depth=DFS(root)

