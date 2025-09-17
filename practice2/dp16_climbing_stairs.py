#dp16_ClimbingStairs.py

n=int(input("enter the steps of stairs:"))

def climbingstairs(n,dp)->int:
	if n<1:
		return 0
	elif n==1:
		dp[n]=1
	elif n==2:
		dp[n]=2
	else:
		dp[n]=climbingstairs(n-1,dp)+climbingstairs(n-2,dp)
	return dp[n]

#bottom up
dp=[0 for _ in range(n+1)]
# for i in range(n+1):
# 	if i==0:
# 		print("enter the step no >0")
# 	elif i==1:
# 		dp[i]=1
# 	elif i==2:
# 		dp[i]=2
# 	else:
# 		dp[i]=dp[i-1]+dp[i-2]
# print(dp[n])

print(climbingstairs(n,dp))
