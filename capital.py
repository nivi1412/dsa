#capital.py
#make first letters of each first letter as capital and if the letters are already capital let them be capital 
#if all alphbet are capital let them be capital but if first letter is small and any other words are capital make them small

def title():
	text=input('enter the sentense:')
	text=text.split()
	result=''
	count=0

	for word in text:
		if 'a' <= word[0] <= 'z': 
			result=result+chr(ord(word[0])- 32)
			for letter in word[1:]:
				if 'A' <= letter <='Z':
					result=result+chr(ord(letter) + 32)
				else:
					result=result+letter
		else:
			for letter in word:
				if 'A' <= letter <= 'Z':
					count+=1
				else:
					count=0
					break
			if count == len(word):
				result=result+word
			if count==0:
				result=result+word[0]
				for letter in word[1:]:
					if 'A' <= letter <='Z':
						result=result+chr(ord(letter) + 32)	
					else:
						result=result+letter

		result=result+" "

	print(result)

testca=int(input("enter number of test cases:"))
for i in range(testca):
	title()