#happy.py
#if in a string os alphabet if there is contiguous vowels strictly >2 print happy else sad


def Vowel():
	string=input("enter the string input:")
	count=0
	bool=False

	for letter in string:
		if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' ):
			count+=1
			if count > 2:
				bool=True
				break
		else:
			count=0
	if bool :print("HAPPYYYY")
	else: print("SADDDDD")

testcase=int(input("enter number of testcases:"))
for i in range(testcase):
	Vowel()
