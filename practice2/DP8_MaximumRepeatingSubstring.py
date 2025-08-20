#DP8_MaximumRepeatingSubstring.py

sequence = input("enter the seq string: ")
word = input("enter the word string: ")
count=0
answer=0
i=0
if len(word)>0 and len(sequence)>0:
	while(i<len(sequence)):
		print(sequence[i:i+len(word)],word)
		if sequence[i:i+len(word)]==word:
			count+=1
			i+=1
		else:
			count=0
			i+=1
		answer=max(count,answer)

	print(answer)
else:
	print("enter length >0")



