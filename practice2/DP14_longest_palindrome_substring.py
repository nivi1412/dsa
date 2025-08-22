#DP14_longest_palindrome_substring.py

# write return type for function 
# for every if there should be a return condition
# no need to save all the palindromes in a list just need to display the maximum length
# didnt write the main condition string[i]==string[j] case at all
# dont keep updating the common variable in recursion

def is_palindrome(string,i,j,dp)->int:
	if dp[i][j]!=-1:
		return dp[i][j]
	else:
		if i==j:
			dp[i][j]=1
		elif j==i+1:
			dp[i][j] = 1 if string[i]==string[j] else 0
		elif j<i: 
			dp[i][j]=0
		else:
			dp[i][j] = 1 if string[i]==string[j] and is_palindrome(string, i+1, j-1, dp) else 0
		return dp[i][j]

pal=input("enter the string:")
prev_answer=''

dp=[[-1 for _ in range(len(pal))] for _ in range(len(pal))]

for i in range(len(pal)):
	for j in range(len(pal)):
		if is_palindrome(pal,i,j,dp):
			if len(pal[i:j+1])>len(prev_answer):
				prev_answer=pal[i:j+1]

print(dp)
print(prev_answer)
