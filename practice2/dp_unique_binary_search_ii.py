#dp_unique_binary_searchII.py

class tree:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def unique_binary_search(mylist,dp)->list[tree]:
	if tuple(mylist) in dp:
		return dp[tuple(mylist)]
	if len(mylist)==0:
		dp[tuple(mylist)]=[None]
	if len(mylist)==1:
		dp[tuple(mylist)]=[tree([mylist[0]])]
	else:
		finallist=[]
		for i in range(len(mylist)):
			left=unique_binary_search(mylist[:i],dp)
			right=unique_binary_search(mylist[i+1:],dp)
			print(left)
			print(right)
			for l in left:
				for r in right:
					root=tree(mylist[i])
					root.left=l
					root.right=r
					finallist.append(root)
		dp[tuple(mylist)]=finallist
	return dp[tuple(mylist)]


n=int(input("enter the node count: "))
dp={}

mylist=[i+1 for i in range(n)]
unique_binary_search(mylist,dp)
print(dp)