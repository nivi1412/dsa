# DP_longest_unequal_adjacent
#solved greedily

import ast

word=input("enter the words array: ")
groups=input("enter the groups array: ")

words=ast.literal_eval(word)
groups=ast.literal_eval(groups)

# bottoms up
answer=[]

if groups[0]==0:
	flag_zero=True
	flag_one=False

else:
	flag_zero=False
	flag_one=True

for i in range(len(groups)):
	print(i)
	if groups[i]==0 and flag_zero:
		answer.append(words[i])
		flag_zero=False
		flag_one=True
	if groups[i]==1 and flag_one:
		answer.append(words[i])
		flag_zero=True
		flag_one=False

print(answer)




