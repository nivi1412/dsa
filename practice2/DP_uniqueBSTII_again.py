#DP_uniqueBSTII_again.py
#we should do dp for root(i guess) not for length. , if we do for length then pappu lo kaalu will happen
#no idea how to do dp 
 	
# Return list of trees instead of list of list of numbers
# DP on (start, end) tuple instead of full list
#tried answer is not coming issue: leftlist=[ then start end what should we keep?]

# start & end pampichinappudu, do not pass list again
# Memory for each tree node of each tree
# List appending inside for loop, but list creation outside for loop


class tree:
	def __init__(self,data):
		self.data=data
		self.left=None 
		self.right=None

my_list=[]

def uniqueBSTII(dp,start,end):
	if (start,end) in dp:
		return dp[(start,end)]
	if start>end:
		return [[None]]
	elif start==end:
		return [[tree(my_list[start])]]

	treelist=[]
	for i in range(start,end+1,+1):
		left=uniqueBSTII(dp,start,i-1)
		right=uniqueBSTII(dp,i+1,end)
		for l in left:
			for r in right:
				root=tree(my_list[i])
				root.left = l
				root.right = r
				treelist.append(root.data)
	dp[(start,end)]=treelist
	return treelist

n=int(input("enter no of nodes: "))
dp={}
for i in range(n):
	my_list.append(i+1)
# start=my_list[0]
# end=my_list[-1]
# dp[(start,end)]=my_list
print(uniqueBSTII(dp,start=0,end=n-1))
