# DP_LongestPalindromicSubstring.py

s=input("enter the string:")
dp=[[0 for _ in range(len(s))]for _ in range(len(s[0]))]

for i in range(len(s)-1,-1,-1):
	for j in range(i,len(s[0]),+1):
		print(i,j)
		# if i==j:
		# 	dp[i][j]=1
		# elif j==i+1:
		# 	if s[i]==s[j]:
		# 		dp[i][j]=1
		# 	else:
		# 		dp[i][j]=0
		# elif j<i:
		# 	continue
		# else:


