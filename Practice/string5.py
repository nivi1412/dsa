#makepalindrome.py
#given a string make tell if its palindrome if one word is removed.

string=input("enter the palindrome to be checked")
i=0
j=len(string)-1
flag=True
palindrome=True

if len(string)==0:
	print(0)
	palindrome=False
elif len(string)==1:
	print(1)
else:
	for letter in range(len(string)//2):
		if string[i]==string[j]:
			i+=1
			j-=1
		else:
			if string[i+2]==string[j]:
				i=i+2
				j=j-1
				flag=False
			elif string[i]==string[j-2]:
				i=i+1
				j=j-2
				flag=False
			else:
				print(0)
				palindrome=False
				break
if palindrome:
	print(1)

