#string1.py
#amazingsubstrings.py
#inp:abedc substrings: a, ab, abe, abed, abedc, e,ed,edc
#return the count of amazing substrings

inp=input("enter the string for substrings:")
count=0
for i in inp:
	if i=="a" or i=="e" or i == "i" or i=="o" or i == "u":
		print(inp)
		print(len(inp))
		count=count+len(inp)
		inp=inp.replace(i,"")
	else:
		inp=inp.replace(i,"")
print(count)
