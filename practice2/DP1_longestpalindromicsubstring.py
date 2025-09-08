#DP1_longestpalindromicsubstring.py

def LPS(s,dp):
	prev_ans=''
	for i in range(len(dp)-1,-1,-1):
		for j in range(i,len(dp),+1):
			if i==j:
				dp[i][j]=1
			if j<i:
				continue
			if j==i+1 and s[j]==s[i]:
				dp[i][j]= 1
			if j>i:
				if s[i]==s[j]:
					dp[i][j]=1+dp[i-1][j-1]
					if len(s[i:j+1]) > len(prev_ans):
						prev_ans=s[i:j+1]
				else:
					dp[i][j]=1+max(dp[i-1][j],dp[i][j-1])
	return prev_ans


s = input("enter the string: ")

dp=[[0 for _ in range(len(s))] for _ in range(len(s))]

print(LPS(s,dp))