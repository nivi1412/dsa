#stringpalindrome.py
#wap to find if the given string is palindrome
#adcda

def palindrom(string):
	for i in range(len(string)//2):
		j= len(string)-1-i
		print(string[i])
		print(string[j])
		if(string[i]!=string[j]):
			return False
	return True


string = input("enter a string:")
string_len = len(string)

pal=palindrom(string)
if(pal):
	print("string is palindrome")
else:
	print("not a palindrome")



