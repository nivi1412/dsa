# DP_Unique_paths.py

def uniquepaths(dp,m,n)->int:
	if m<0 or n<0 or m>=len(dp) or n>=len(dp[0]):
		return 0
	if (n==0)or (m==0):
		return 1
	dp[m][n]=uniquepaths(dp,m-1,n)+uniquepaths(dp,m,n-1)
	return dp[m][n]


m=int(input("enter no of rows: "))
n=int(input("enter no of cols: "))
dp=[[0 for _ in range(n)] for _ in range(m)]

#bottoms up

# for i in range(1,m):
# 	dp[i][0]=1
# for j in range(1,n):
# 	dp[0][j]=1

# for i in range(1,m):
# 	for j in range(1,n):
# 		dp[i][j]=dp[i-1][j]+dp[i][j-1]

# print(dp[m-1][n-1])

#tops down

print(uniquepaths(dp,m-1,n-1))