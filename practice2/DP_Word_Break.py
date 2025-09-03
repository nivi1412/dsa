#DP_Word_Break.py
import ast

s=input("enter the string: ")
worddict=input("enter the worddict: ")
worddict=ast.literal_eval(worddict)

dp=[False for _ in range(len(s)+1)]

dp[0]=True

for i in range(1,len(s)+1):
	for j in range(i+1):
		if s[j:i] in worddict and dp[j]:
			print(s[j:i], dp[j],j)
			dp[i]= True
print("dp:",dp)
print(dp[-1])
