# DP_LongestPalindromicSubstring.py

def longpal(s,i,j,dp)->int:
	if i<0 or j<0 or i>len(s) or j>len(s):
		return 0
	if dp[i][j]!=-1:
		return dp[i][j]
	else:
		if i==j:
			dp[i][j]=1
		elif j==i+1:
			dp[i][j]=1 if s[i]==s[j] else 0
		elif j<i:
			dp[i][j]=0
		else:
			dp[i][j]=1+longpal(s,i-1,j-1,dp) if s[i]==s[j] else max(longpal(s,i-1,j,dp),longpal(s,i-1,j,dp))
		return dp[i][j]

s=input("enter the string:")
dp=[[-1 for _ in range(len(s))]for _ in range(len(s))]
prev_ans=''
#top down
for i in range(len(s)):
	for j in range(len(s)):
		prev_ans=s[i:j+1] if longpal(s,i,j,dp) and len(s[i:j+1])>len(prev_ans) else prev_ans

print(prev_ans)


#bottoms up
# dp=[[0 for _ in range(len(s))]for _ in range(len(s))]
# prev_ans=''
# for i in range(len(s)-1,-1,-1):
# 	for j in range(i,len(s),+1):
# 		if i==j:
# 			dp[i][j]=1
# 		elif j==i+1:
# 			if s[i]==s[j]:
# 				dp[i][j]=1
# 			else:
# 				dp[i][j]=0
# 		elif j<i:
# 			continue
# 		else:
# 			if s[i]==s[j]:
# 				dp[i][j]=1+dp[i-1][j-1]
# 				if len(s[i:j+1])>len(prev_ans):
# 					prev_ans=s[i:j+1]
# 			else:
# 				dp[i][j]=max(dp[i-1][j],dp[i][j-1])

# print(prev_ans)


