# dp_reg_exp_matching.py
# "mississippi" ------> "mis*is*p*."
# "aaaaaaaaaaaab" ------> "a*aab"

s=input("enter the input string:")
p=input("enter the pattern:")

dp=True

i=0
j=0
len1=len(s)-1
len2=len(p)-1

while ((i<len1) and (j<len2) and dp):
	if s[i]==p[j] and p[j]=='.':
		dp=dp and True
	elif p[j]=='*' and j-1>=0:
		if p[j-1]==s[]
















