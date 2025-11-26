# robber.py
import ast

# nums=input("enter the houses array:")
# nums=ast.literal_eval(nums)
# dp=[0 for _ in range(len(nums))]

# if len(nums)==1:
# 	dp[0]=nums[0]
# if len(nums)>=2:
# 	dp[0]=nums[0]
# 	dp[1]=max(nums[0],nums[1])

# 	for i in range(2,len(nums)):
# 		dp[i]=max(dp[i-2]+nums[i],dp[i-1])

# print(dp)
# print(dp[-1])

# -------------------if round houses ---------------------------

def max_nums(nums,dp):
	if len(nums)==1:
		dp[0]=nums[0]
	if len(nums)>=2:
		dp[0]=nums[0]
		dp[1]=max(nums[0],nums[1])

		for i in range(2,len(nums)):
			dp[i]=max(dp[i-2]+nums[i],dp[i-1])
			print(dp)
	return dp[-1]



nums=input("enter the houses:")
nums=ast.literal_eval(nums)
nums1=nums[:len(nums)-1]
nums2=nums[1:len(nums)]

dp1=[0 for _ in range(len(nums1))]
dp2=[0 for _ in range(len(nums2))]

print(max(max_nums(nums1,dp1),max_nums(nums2,dp2)))

