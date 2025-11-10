#wordbreak.py
import ast

s=input("enter the string: ")
worddict=input("enter the word dictionary: ")
worddict=ast.literal_eval(worddict)
dp=[False for _ in range(len(s)+1)]
dp[0]=True

for i in range(len(s)):
	for j in range(i+1):
		print(s[j:i+1],dp)
		if dp[j] and s[j:i+1] in worddict:
			dp[i+1]=True
			print(dp)


for i in range(len(s)):
	for 