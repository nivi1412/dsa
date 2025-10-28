#edit_distance.py

word1=input("enter word1: ")
word2=input("enter word2: ")

dp=[[0 for _ in range(len(word2))] for _ in range(len(word1))]

dp[0][0]=1 if word1[0]!=word2[0] else dp[0][0]

for i in range(1,len(word1)):
	dp[i][0]=1+dp[i-1][0] if word1[i]!=word2[0] else dp[i-1][0]

for i in range(1,len(word2)):
	dp[0][i]=1+dp[0][i-1] if word2[i]!=word1[0] else dp[0][i-1]

for i in range(1,len(word1)):
	for j in range(1,len(word2)):
		dp[i][j]=dp[i-1][j-1] if word1[i]==word2[j] else 1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])