#DP12_longestunequal_subsequentgroups.py
import ast

words=input("enter words array:")
groups=input("enter groups array:")

words=ast.literal_eval(words)
groups=ast.literal_eval(groups)

answer=[]
answer.append(words[0])
flag_one=False
flag_zero=False

if groups[0]==1:
	flag_zero=True
	for i in range(1,len(groups),+1):
		if groups[i]==0 and flag_zero:
			answer.append(words[i])
			flag_one=True
			flag_zero=False
		if groups[i]==1 and flag_one==True:
			answer.append(words[i])	
			flag_zero=True
			flag_one=False
else:
	flag_one=True
	for i in range(1,len(groups),+1):
		if groups[i]==1 and flag_one==True:
			answer.append(words[i])
			flag_zero=True
			flag_one=False
		if groups[i]==0 and flag_zero:
			answer.append(words[i])
			flag_one=True
			flag_zero=False


print(answer)