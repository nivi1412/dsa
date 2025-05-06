#roman to decimal
inp=input("enter the roman numbers:")
inp=inp[::-1]
print(inp)

roman_map={'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

total=0
prev_value=0

for char in inp:
	value=roman_map[char]
	if value<prev_value:
		total-=value
	else:
		total+=value
	prev_value=value
print(total)






