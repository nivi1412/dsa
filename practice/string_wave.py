#stringwave.py
# You are given a string S and an integer numRows. Your task is to print the string in a wave-like (zigzag) pattern across the given number of rows and 
# return the output row-wise.Characters should be placed one per row in a cyclic downward pattern until all characters are placed.
# The string flows row by row like a vertical wave.
#S = "ABCDEFGHI"
#numRows = 3
#output:
# ADG
# BEH
# CFI

string=input("enter the string:")
rows=int(input("enter no of rows:"))
stack=[]

for i in range(rows):
	stack.append('')
j=0
i=0
increment=True

while(j<rows and i<len(string)):
	print(i,j)
	stack[j]=stack[j]+string[i]
	if increment:
		if j==rows-1:
			increment=False
			j-=1
		else:
			j+=1

	else:
		if j==0:
			increment=True
			j+=1
		else:
			j-=1

	i+=1
for i in stack:
	print(i)

	

