#unique_bst.py

def unique_BST(start,end,dp):
	if (start,end) in dp:
		return dp[(start,end)]
	if start>=end:
		return 1

	finalcount=0
	for i in range(start,end+1):
		left_count=unique_BST(start,i-1,dp)
		right_count=unique_BST(i+1,end,dp)
		finalcount+=left_count*right_count
	dp[(start,end)]=finalcount
	return dp[(start,end)]

n=int(input("enter the node count:"))
dp={}
start=0
end=n-1

print(unique_BST(start,end,dp))