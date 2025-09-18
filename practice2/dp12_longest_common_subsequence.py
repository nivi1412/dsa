#DP12_longest_common_subsequence.py
m=input("enter first string: ")
n=input("enter second string: ")

#easy method:

# dp=[[0 for _ in range(len(n)+1)]for _ in range(len(m)+1)]

# for i in range(1,len(dp),+1):
# 	for j in range(1,len(dp[0]),+1):
# 		print(i,j)
# 		if m[i-1]==n[j-1]:
# 			dp[i][j]=1+dp[i-1][j-1]
# 		else:
# 			dp[i][j]=max(dp[i-1][j],dp[i][j-1])

# print(dp)
# print(dp[len(m)][len(n)])

# # rahul fav method:
# #if we have to avoid edge cases we should write cases if i-1<0 , j-1<0
# #if we write that then dp[-1][j] we didnt initialize how to manage it?
dp=[[0 for _ in range(len(n))]for _ in range(len(m))]

# #base cases:
for i in range(len(m)):
	dp[i][0] = 1 if n[0] in m[0:i+1] else 0

for j in range(len(n)):
	dp[0][j] = 1 if m[0] in n[0:j+1] else 0

for i in range(1, len(m), +1):
	for j in range(1, len(n), +1):
		if m[i]==n[j]:
			dp[i][j]=1+dp[i-1][j-1]
		else:
			dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[len(m)-1][len(n)-1])