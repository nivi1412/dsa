#DP_divisorgame.py

def find_factor(num)->list:
	factor=[]
	for i in range(1,num):
		if num%i==0:
			factor.append(i)
	return factor

def divisor_game(n,dp)->bool:
	if n in dp:
		return dp[n]
	if n==1:
		dp[n]=False
	elif n==2:
		dp[n]=True
	else:
		for factor in find_factor(n):
			dp[n]=dp[n] or (not divisor_game((n-factor),dp))
	return dp[n]
	
n=int(input("enter the number:"))
dp=[False for _ in range(n+1)]

# bottoms up
# for i in range(1,n+1,+1):
# 	if i==1:
# 		dp[i]=False
# 	elif i==2:
# 		dp[i]=True
# 	else:
# 		for factor in find_factor(i):
# 			print(factor)
# 			dp[i] = dp[i] or (not dp[i-factor])

# print(dp[-1])

#top down 
divisor_game(n,dp)
print(dp[n])