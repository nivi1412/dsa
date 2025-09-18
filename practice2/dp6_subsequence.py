#DP6_Subsequence.py
#no idea where to apply dp
#tim complexity o(t)

def subsequence(s,t):
	i,j=0,0
	while(j<len(t)):
		if s[i]==t[j]:
			i+=1
			j+=1
		else:
			j+=1
	print(i)
	if i==len(s):
		return(True)
	else:
		return False

s=input("enter the 1st subsequence: ")
t=input("enter the 2nd subsequence: ")

if len(s)>len(t):
	print(False)
else:
	print(subsequence(s,t))