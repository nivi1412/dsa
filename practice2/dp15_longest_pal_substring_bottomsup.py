# DP15_longest_Pal_substring_bottomsup.py

pal=input("enter the string:")

dp=[[0 for _ in range(len(pal))] for _ in range(len(pal))]
answer=[]
prev_answer=''
for i in range(len(pal)-1,-1,-1):
	for j in range(i,len(pal),+1):
		if i==j:
			dp[i][j]=1
		elif j==i+1:
			dp[i][j]=1 if pal[i]==pal[j] else 0
		elif j<i:
			continue
		else:
			dp[i][j]=1 if (pal[i]==pal[j] and dp[i+1][j-1]) else 0
		prev_answer=pal[i:j+1] if len(pal[i:j+1])>len(prev_answer) and dp[i][j]==1 else prev_answer
print(prev_answer)

		
