#greedy_couple_holding_hands.py
import ast

row=input("enter the row array:")
row=ast.literal_eval(row)

pos={}

for i in range(len(row)):
	pos[row[i]]=i

x=0
y=1
swap_count=0

while(y<len(row)):
	print(row[x],row[y])
	print(row)
	if row[x]!=row[y]^1:
		row[pos[x^1]],row[y]=row[y],row[pos[x^1]]
		swap_count+=1
	x+=2
	y+=2

print(swap_count)