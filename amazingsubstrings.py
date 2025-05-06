#amazingsubstrings.py
#inp:abedc substrings: a, ab, abe, abed, abedc, e,ed,edc

def substring(inp):
	count=0
	j=len(inp)
	print(inp)
	for i in range(j):
		if(inp[i] == 'A' or inp[i] == 'E' or inp[i] == 'I' or inp[i] == 'O' or inp[i] == 'U'):
			print(inp[i])
			print("j",j)
			count=count+(j-i)
			print("count",count)
	return count

inp=input("enter the string")
count=substring(inp)
print(count)