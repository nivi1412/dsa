#DP_uniqueBST1.py

# Instead of passing full list, just passing the length of list is also sufficient
def count_BST(n,dp)->input:
	if n in dp:
		return dp[n]
	if n==0 or n==1:
		dp[n]=1
	else:
		count=0
		for i in range(n):
			print("l:",i)
			print("r:",n-i-1)
			left=count_BST(i,dp)
			right=count_BST(n-i-1,dp)
			count+=left*right
		dp[n]=count
	return dp[n]

n=int(input("enter the node count: "))
dp={}
print(count_BST(n,dp))


# def count_BST(my_list,dp)->input:
# 	if len(my_list) in dp:
# 		return dp[len(my_list)]
# 	if len(my_list)==0 or len(my_list)==1:
# 		dp[0]=1
# 		dp[1]=1
# 	else:
# 		count=0
# 		for i in range(len(my_list)):
# 			print("l:",my_list[:i])
# 			print("r:",my_list[i+1:])
# 			left=count_BST(my_list[:i],dp)
# 			right=count_BST(my_list[i+1:],dp)
# 			count+=left*right
# 		dp[len(my_list)]=count
# 	return dp[len(my_list)]

# n=int(input("enter the node count: "))
# my_list=[]
# dp={}
# for i in range(n):
# 	my_list.append(i+1)

# print(count_BST(my_list,dp))