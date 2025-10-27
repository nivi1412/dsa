#longest_pal_substring.py

s=input("enter the string: ")

dp=[[False for _ in range(len(s))]for _ in range(len(s))]
# print(dp)

prev_String=''
for i in range(len(s)-1,-1,-1):
	for j in range(i,len(s),+1):
		if i==j:
			dp[i][j]=True
		elif j==i+1:
			dp[i][j]=True if s[i]==s[j] else dp[i][j]	
		elif j<i:
			continue
		elif j>i:
			dp[i][j]=True if s[i]==s[j] and dp[i+1][j-1] else dp[i][j]

		if dp[i][j] and len(s[i:j+1])>len(prev_String):
			prev_String=s[i:j+1]


print(prev_String)