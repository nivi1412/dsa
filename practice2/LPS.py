# LPS.py

s=input("enter the string: ")

dp=[[0 for _ in range(len(s))]for _ in range(len(s))]

prev_ans=''
for i in range(len(s),-1,-1):
	for j in range(i,len(s),+1):
		print("i,j:",i,j,s[i:j+1])
		if i==j:
			dp[i][j]=1
		elif j<i:
			continue
		else:
			if s[i]==s[j]:
				dp[i][j]=1+dp[i-1][j-1]
				if len(s[i:j+1])> len(prev_ans):
					prev_ans=s[i:j+1]
			else:
				dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp)
print(prev_ans)