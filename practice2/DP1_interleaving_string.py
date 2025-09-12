# DP1_interleaving_string.py
#why for base case we are comparing one string with the s3 but in main case 

s1=input("enter s1: ")
s2=input("enter s2: ")
s3=input("enter s3: ")

dp=[[0 for _ in range(len(s2))] for _ in range(len(s1))]
dp[0][0]=True

for i in range(1,len(s1)):
	dp[i][0]=True if s1[:i+1]==s3[:i+1] else False

for j in range(1,len(s2)):
	dp[0][j]=True if s2[:j+1]==s3[:j+1] else False

for i in range(1,len(s1)):
	for j in range(1,len(s2)):
		a=True if s1[i-1]==s3[i+j-1] and dp[i-1][j] else False
		b=True if s2[j-1]==s3[i+j-1] and dp[i][j-1] else False
		dp[i][j]=a or b

print(dp)
print(dp[i-1][j-1])