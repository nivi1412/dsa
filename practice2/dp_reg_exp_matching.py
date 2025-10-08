# dp_reg_exp_matching.py
# "mississippi" ------> "mis*is*p*."
# "a*aaaaaaaaaaa" ------> "aaab"

s=input("enter the input string:")
p=input("enter the pattern:")

dp=True


for i in range(len(p)):
	if dp:
		if (p[i]=='.' or s[i]==p[i]):
			dp = dp and True
		if p[i]=='*' and i-1 >=0:
			local=''
			local+=p[i-1]+p[i]
			










