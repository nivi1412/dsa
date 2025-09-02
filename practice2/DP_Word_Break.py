#DP_Word_Break.py
import ast

s=input("enter the string: ")
worddict=input("enter the worddict: ")
worddict=ast.literal_eval(worddict)

dp=[False for _ in range(len(s)+1)]

dp[0]=True

for i in range(1,len(s)+1):
	for j in range(i+1):
		if s[j:i+1] in worddict:
			dp[i]=dp[i] or True
