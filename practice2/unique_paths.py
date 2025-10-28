# unique_paths.py

m=int(input("enter the row: "))
n=int(input("enter the column: "))

dp=[[0 for _ in range(n)]for _ in range(m)]

for i in range(m):
	dp[i][0]=1

for j in range(n):
	dp[0][j]=1

for i in range(1,m):
	for j in range(1,n):
		dp[i][j]=dp[i-1][j]+dp[i][j-1]

print(dp[-1][-1])