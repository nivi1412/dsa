# dp_editdistance.py

word1=input("enter the first word:")
word2=input("enter the second word:")

dp=[[0 for _ in range(len(word2))] for _ in range(len(word1))]

dp[0][0]=1 if word1[0]!=word2[0] else 0

for i in range(1,len(word1)):
	dp[i][0]=1+dp[i-1][0] if word1[i]!=word2[0] else dp[i-1][0]

for j in range(1,len(word2)):
	dp[0][j]=1+dp[0][j-1] if word1[0]!=word2[j] else dp[0][j-1]

for i in range(1,len(word1)):
	for j in range(1,len(word2)):
		if word1[i]==word2[j]:
			dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
		else:
			dp[i][j]=1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])

print(dp[-1][-1])
