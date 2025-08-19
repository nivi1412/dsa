#DP8_MaximumRepeatingSubstring.py

def substringcount(sequence,word):
	count=0
	if word in sequence:
		count+=1
		sequence=sequence.replace(word,"",1)
		print(sequence)
		count=count+substringcount(sequence,word)
	return count

sequence = input("enter the seq string: ")
word = input("enter the word string: ")

print(substringcount(sequence,word))


