#DP8_MaximumRepeatingSubstring.py

sequence = input("enter the seq string: ")
word = input("enter the word string: ")

dp=[0]*len(sequence)

for i in range(len(sequence)):
	if i < len(word)-1:
		dp[i]=0
	else:
		j=i-(len(word)-1)
		if sequence[j:j+len(word)]==word:
			print(sequence[j:j+len(word)],word)
			dp[i]=1+dp[i-(len(word))]
		else:
			dp[i]=0
print(dp)
print(max(dp))



