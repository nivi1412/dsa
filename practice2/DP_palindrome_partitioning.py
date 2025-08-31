#DP_palindrome_partitioning.py

def is_palindrome(s,start,end):
	if start==end:
		return True
	if end>start:
		if s[start]==s[end]:
			return is_palindrome(s,start+1,end-1)

s=input("enter the string: ")

# dp[i] => List of possible palindrome partitioning for s[0:i] => List of lists


print(dp)

