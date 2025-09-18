#string3.py
#encodebitstostring
#00:A 01:T 10:G 11:C

inp=input("enter the bits to be encoded")
result=[]
for i in range(0,len(inp),+2):
	result.append(inp[i:i+2])
encode=''
for i in result:
	if i=="00":
		encode=encode+'A'
	elif i=="01":
		encode=encode+'T'
	elif i=="10":
		encode=encode+'G'
	elif i=="11":
		encode=encode+'C'
	else:
		pass
print(encode)
