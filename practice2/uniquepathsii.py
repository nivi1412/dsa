# uniquepathsii.py
import ast

OG=input("enter the frid coordinates: ")
OG=ast.literal_eval(OG)

dp=[[0 for _ in range(len(OG[0]))] for _ in range(len(OG))]

for i in range(len(OG)):
	if OG[i][0]==0:
		dp[i][0]=1

for j in range(len(OG[0])):
	if OG[0][j]==0:
		dp[0][j]=1

for i in range(1,len(OG)):
	for j in range(1,len(OG[0])):
		dp[i][j]=dp[i-1][j]+dp[i][j-1] if not OG[i][j] else dp[i][j]

print(dp[-1][-1])