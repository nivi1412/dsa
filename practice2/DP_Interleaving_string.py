#DP_Interleaving_string.py

s1=input("enter the 1st string: ")
s2=input("enter the 2nd string: ")
s3=input("enter the 3rd string: ")

if len(s3)==len(s1)+len(s2):
	dp=[[False for _ in range(len(s2)+1)]for _ in range(len(s1)+1)]
	dp[0][0]=True
	for i in range(1,len(s1)+1):
		dp[i][0]=True if s1[:i]==s3[:i] else False

	for j in range(1,len(s2)+1):
		dp[0][j]=True if s2[:j]==s3[:j] else False

	for i in range(1,len(s1)+1):
		for j in range(1,len(s2)+1):
			a=True if s1[i-1]==s3[i+j-1] and dp[i-1][j] else False
			b=True if s2[j-1]==s3[i+j-1] and dp[i][j-1] else False
			dp[i][j]=a or b


else:
	print(False)


print(dp[len(s1)][len(s2)])