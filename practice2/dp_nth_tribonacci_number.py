#DP_Nth_Tribonacci_Number.py

def tribonacci(n,dp)->int:
	if n in dp:
		return dp[n]
	if n==1 or n==1 or n==2:
		return dp[n]
	dp[n]=tribonacci(n-1,dp)+tribonacci(n-2,dp)+tribonacci(n-3,dp)
	return dp[n]

n=int(input("enter the tribonacci number:"))
dp=[0 for _ in range(n+1)]
dp[0]=0
dp[1]=1
dp[2]=1
#bottoms up
# for i in range(n+1):
# 	if i==0:
# 		dp[i]=0
# 	elif i==1:
# 		dp[i]=1
# 	elif i==2:
# 		dp[i]=1
# 	else:
# 		dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

# print(dp[n])

#top down
print(tribonacci(n,dp))
