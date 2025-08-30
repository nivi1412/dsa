#DP_Decode_ways.py

s=input("enter the string: ")
dp=[0 for _ in range(len(s))]

dp[0]=1 if 1<=int(s[0])<=9 else 0

a=1 if 1<=int(s[0])<=9 and 1<=int(s[1])<=9 else 0
c=1 if 10<=int(s[:2])<=26 else 0

dp[1]=a+c

for i in range(2,len(s),+1):
	a=1 if 1<=int(s[i])<=9 else 0
	b=1 if 10<=int(s[i-1:i+1])<=26 else 0
	dp[i]=dp[i-1]*a+dp[i-2]*b
print(dp)