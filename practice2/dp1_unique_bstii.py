# DP1_unique_BSTII.py
from build_binarytree import print_binarytree

class tree():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def unique_BST(dp,start,end):
	if (start,end) in dp:
		return dp[(start,end)]
	if start == end:
		dp[(start,end)]=[tree(start+1)]
		return dp[(start,end)]
	elif start > end:
		dp[(start,end)]=[None]
		return dp[(start,end)]
	elif start < end:
		final_list=[]
		for i in range(start,end+1):
			left=unique_BST(dp,start,i-1)
			right=unique_BST(dp,i+1,end)
			for l in left:
				for r in right:
					root=tree(i+1)
					root.left=l
					root.right=r
					final_list.append(root)
		dp[(start,end)]=final_list
		return final_list




n=int(input("enter the node count: "))
my_list=[]
dp={}
for i in range(n):
	my_list.append(i+1)

unique_BST(dp,start=0,end=len(my_list)-1)
# 	print_binarytree(i)