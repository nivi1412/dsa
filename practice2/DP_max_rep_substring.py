#DP_max_rep_substring.py

def maxrep(i,sequence,word,dp)->int:
	if dp[i]!=-1:
		return dp[i]
	elif i<0:
		return 0
	else:
		if sequence[i:i+len(word)]==word:
			print(sequence[i:i+len(word)],word)
			dp[i]=1+maxrep(i-len(word),sequence,word,dp)
		else:
			dp[i]=0
	print("i,dp[i]:",i,dp[i])
	return dp[i]

sequence=input("enter the sequence: ")
word=input("enter the word: ")
#top sown dp init
dp=[-1 for _ in range(len(sequence))]

# dp=[0 for _ in range(len(sequence))]

# # bottoms up
# for i in range(len(sequence)):
# 	if sequence[i:i+len(word)]==word:
# 		dp[i]=1+dp[i-len(word)]

# print(max(dp))

#top down
for i in range(len(sequence)):
	maxrep(i,sequence,word,dp)
print(max(dp))
