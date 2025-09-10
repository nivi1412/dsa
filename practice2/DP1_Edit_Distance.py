# DP1_Edit_Distance.py

word1=input("enter the 1st word: ")
word2=input("enter the 2nd word: ")

dp=[[0 for _ in range(len(word2))]for _ in range(len(word1))]
dp[0][0]=0 if word1[0]==word2[0] else 1

for i in range(1,len(word1)):
	if word2[0] in word1[:i+1]:
		dp[i][0]=i
	else:
		dp[i][0]=1+i

print(dp)

for j in range(1,len(word2)):
	if word1[0] in word2[:j+1]:
		dp[0][j]=j
	else:
		dp[0][j]=1+j

print(dp)

for i in range(1,len(word1)):
	for j in range(1,len(word2)):
		if word1[i]==word2 [j]:
			dp[i][j]=dp[i-1][j-1]
		else:
			dp[i][j]=1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
print(dp[len(word1)-1][len(word2)-1])

