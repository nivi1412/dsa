#array4.py
#convert 1 and 0 in an array into a decimal number


inp=input("enter array of decimal digits:")
inp=list(map(int,inp.split()))
decimal=0
j=0
for i in range(len(inp)-1,-1,-1):
	decimal=decimal+(inp[j]*(2**i))
	j+=1

print(decimal)

