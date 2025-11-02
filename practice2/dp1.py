#dp1.py
s=input("enter the string: ")
dp=[[False for _ in range(len(s))] for _ in range(len(s))]

ans=''
for i in range(len(s)-1,-1,-1):
	for j in range(i, len(s)):
		if i==j:
			dp[i][j]=True
		elif j==i+1:
			dp[i][j]=True if s[i]==s[j] else False
		elif j<i:
			continue
		else:
			dp[i][j]=True if s[i]==s[j] and dp[i+1][j-1] else False
		if dp[i][j] and len(s[i:j+1])>len(ans):
			ans=s[i:j+1]


print(dp)
print(ans)

