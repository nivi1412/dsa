#DP_palindrome_partitioning.py

def is_palindrome(s,start,end):
	if start==end:
		return True
	if end>start:
		if s[start]==s[end]:
			return is_palindrome(s,start+1,end-1)
		else:
			return False
	if end <start:
		return True


s=input("enter the string: ")
# dp[i] => List of possible palindrome partitioning for s[0:i] => List of lists
dp = []
dp.append([[]])

for i in range(1,len(s)+1):
	local=[]
	for j in range(i):
		start=j
		end=i-1
		print(j,i)
		if is_palindrome(s,start,end):
			print(s[start:end+1]) 
			for mylists in dp[j]:
				mylists=mylists.copy()
				mylists.append(s[start:end+1])
				local.append(mylists)
	dp.append(local)
	print(dp)
