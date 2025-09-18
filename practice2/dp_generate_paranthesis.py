# DP_generate_paranthesis.py

def genparanthesis(n,dp):
	if n in dp:
		return dp[n]
	for k in range(1,n+1):
		dp[k]=[]
		for i in range(k):
			for inside in genparanthesis(i,dp):
				for outside in genparanthesis(k-i-1,dp):
					dp[k].append("("+inside+")"+outside)
	return dp[n]



n=int(input("enter the pair of paranthesis: "))

dp={}
dp[0]=[""]

#bottoms up
# for k in range(1,n+1):
# 	dp[k]=[]
# 	for i in range(k):
# 		print("i,k,k-i-1:",i,k,k-i-1)
# 		for inside in dp[i]:
# 			for outside in dp[k-i-1]:
# 				print("i,o:",inside,outside)
# 				dp[k].append("("+inside+")"+outside)

# print(dp)

#top down


print(genparanthesis(n,dp))