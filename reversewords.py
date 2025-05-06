#reversewords.py
#reverse word by word in string

inp=input("enter string input")
inp=inp.split(" ")
result=""
k=len(inp)-1
for i in range(k,-1,-1):
	result=result+inp[i]
	result=result.strip()
	result=result+" "
print(result.strip())

