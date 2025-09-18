#Dp_House_robber_II.py

import ast

nums=input("enter the circle house list:")
nums=ast.literal_eval(nums)

sp1=[nums[i] for i in range(len(nums)-1)]
sp2=[nums[i] for i in range(1,len(nums))]

dp1=[0 for _ in range(len(sp1))]
dp2=[0 for _ in range(len(sp2))]

dp1[0]=sp1[0]
dp2[0]=sp2[0]
dp1[1]=max(sp1[0],sp1[1])
dp2[1]=max(sp2[0],sp2[1])

for i in range(2,len(sp1)):
	dp1[i]=max(dp1[i-1],sp1[i]+dp1[i-2])

for j in range(2,len(sp2)):
	dp2[j]=max(dp2[j-1],sp2[j]+dp2[j-2])

print(dp1)
print(dp2)
print(max(dp1[-1],dp2[-1]))