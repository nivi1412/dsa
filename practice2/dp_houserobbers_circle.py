# dp_houserobbers_circle.py
import ast

nums=input("enter the nums array:")
nums=ast.literal_eval(nums)

# dp=[0 for _ in range(len(nums))]

# dp[0]=nums[0]
# dp[1]=max(dp[0],nums[1])

# for i in range(2,len(nums)):
# 	dp[i]=max(dp[i-1],dp[i-2]+nums[i])

# print(dp[-1])

nums1=nums[:len(nums)-2]
nums2=nums[1:]

dp1=[0 for _ in range(len(nums1))]
dp2=[0 for _ in range(len(nums2))]

dp1[0]=nums1[0]
dp1[1]=max(dp1[0],nums1[1])
dp2[0]=nums2[0]
dp2[1]=max(dp2[0],nums2[1])

for i in range(2,len(nums1)):
	dp1[i]=max(dp1[i-1],dp1[i-2]+nums1[i])

for i in range(2,len(nums2)):
	dp2[i]=max(dp2[i-1],dp2[i-2]+nums2[i])

print(max(dp1[-1],dp2[-1]))