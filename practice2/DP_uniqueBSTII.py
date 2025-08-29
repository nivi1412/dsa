#DP_uniqueBSTII.py
#we should do dp for root(i guess) not for length. , if we do for length then pappu lo kaalu will happen
#no idea how to do dp 

# Return list of trees instead of list of list of numbers
# DP on (start, end) tuple instead of full list

def uniqueBSTII(n,my_list,dp):
	print("my_list:",my_list)
	if my_list in dp:
		return dp[my_list]
	elif n==0:
		dp[my_list]=[["null"]]
	elif n==1:
		dp[my_list]=[[my_list[0]]]
	else:
		finallist=[]
		for i in range(len(my_list)):
			# print("left,right",my_list[:i],"  ",my_list[i+1:])
			left=uniqueBSTII(len(my_list[:i]),my_list[:i],dp)
			right=uniqueBSTII(len(my_list[i+1:]),my_list[i+1:],dp)
			root=my_list[i]
			print(root,":",left,right)
			for k in left:
				for j in right:
					local=[]
					local.append(root)
					for ele1 in k:
						local.append(ele1)
					for ele2 in j:
						local.append(ele2)
					finallist.append(local)
			dp[root]=finallist
	return dp[n]

n=int(input("enter no of nodes: "))
dp={}
my_list=[]
for i in range(n):
	my_list.append(i+1)

uniqueBSTII(n,my_list,dp)
