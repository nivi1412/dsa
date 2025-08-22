# DP15_Longest_Palindromic_Subsequence.py
def is_palindrome(string):
	j=len(string)-1
	is_pal=True
	for i in range(len(string)//2):
		if string[i]==string[j]:
			j-=1
		else:
			is_pal=False
			break
	return is_pal

seq=input("enter the sequence: ")
answer=[]
dp=[[0 for _ in range(len(seq))] for _ in range(len(seq))]

for i in range(len(seq)):
	for j in range(len(seq)-1,-1,-1):
		if i==j:
			dp[i][j]=1
			answer.append(seq[i:j+1])
		elif j==i+1:
			if seq[i]==seq[j]:
				answer.append(seq[i:j+1])
				dp[i][j]=1
		elif j<i:
			continue
		else:
			if is_palindrome(seq[i:j+1]):
				answer.append(seq[i:j+1])
				dp[i][j]=1
print(dp)
print(answer)
