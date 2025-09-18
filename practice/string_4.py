#happy.py
#if in a string os alphabet if there is contiguous vowels strictly >2 print happy else sad

string=input("enter string:")
count=0
for i in string:
	if i == "a" or i== "u" or i=="e" or i=="i" or i=="u":
		count+=1
	else:
		count=0
	if count >2:
		print("Happy")
		break

if count<=2:
	print("sad")

