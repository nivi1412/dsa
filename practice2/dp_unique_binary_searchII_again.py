#dp_unique_binary_searchII_again.py

from build_binarytree import print_binarytree

class tree:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def unique_binary_search(start,end,dp,mylist)->list[tree]:
	if (start,end) in dp:
		return dp[(start,end)]
	if start > end:
		dp[(start,end)]=[None]
	if start==end:
		dp[(start,end)]=[tree(mylist[start])]
	if start<end:
		finallist=[]
		for i in range(start,end+1):
			left=unique_binary_search(start,i-1,dp,mylist)
			right=unique_binary_search(i+1,end,dp,mylist)	
			for l in left:
				for r in right:
					root=tree(mylist[i])
					root.left=l
					root.right=r
					finallist.append(root)
		dp[(start,end)]=finallist
	return dp[(start,end)]


n=int(input("enter the node count: "))
dp={}

mylist=[i+1 for i in range(n)]
start=0
end=len(mylist)-1
for i in unique_binary_search(start,end,dp,mylist):
	print_binarytree(i)
# print(dp)