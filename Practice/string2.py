#string2.py
#capital.py
#make first letters of each first letter as capital and if the letters are already capital let them be capital 
#if all alphbet are capital let them be capital but if first letter is small and any other words are capital make them small

Str=input("enter the string")

Str=Str.split()
result=''
count=0

for words in Str:
	if "a" <= words[0] <= "z":
		result=result+chr(ord(words[0])-32)
		for letter in words[1:]:
			if "A"<=letter<="B":
				result=result+chr(ord(words[0])+32)
			else:
				result=result+letter

	else:
		for letter in words:
			if "a"<=letter<="z":
				count+=1
		if not(count):
			result=result+words
		else:
			result=result+words[0]
			for letter in words[1:]:
				if "A"<=letter<="Z":
					result=result+chr(ord(letter)+32)
				else:
					result=result+letter
	result=result+" "


print(result)
