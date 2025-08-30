#DP_uniqueBSTII_again_again.py

my_list=[]

class tree:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def DP_uniqueBSTII_again_again(start,end,dp):
	if (start,end) in dp:
		return dp[(start,end)]
	if start>end:
		return [[None]]
	elif start==end:
		return [[my_list[start]]]
	else:
		finallist=[]
		for i in range(start,end+1):
			left=DP_uniqueBSTII_again_again(start,i-1,dp)
			right=DP_uniqueBSTII_again_again(i+1,end,dp)
			for l in left:
				for r in right:
					root=tree(my_list[i])
					root.left=l
					root.right=r
					finallist.append(root.data)
		dp[(start,end)]=finallist
		return finallist

n=int(input("enter the node count:"))
dp={}
for i in range(n):
	my_list.append(i+1)
start=0
end=len(my_list)-1
print(DP_uniqueBSTII_again_again(start,end,dp))

