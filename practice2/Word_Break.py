#Word_Break.py
import ast

s=input("enter the string: ")
wordDict=input("enter array: ")
wordDict=ast.literal_eval(wordDict)

dp=[False for _ in range(len(s)+1)]
dp[0]=True

for i in range(1,len(s)+1):
	for j in range(i+1):
		# if s[j:i] in wordDict and dp[j]:
		# 	dp[i]=True
		dp[i]=True if s[j:i] in wordDict and dp[j] else dp[i]
print(dp)


