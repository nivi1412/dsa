#zigzag.py
#store in strings in wafeform format and concatinate those strings and return 

inp=input("enter the string:")
str_len=len(inp)
row_len=int(input("enter no of rows"))
row=['' for _ in range(row_len)]
output_String=""



if row_len==1:
	output_String=inp
elif row_len==0:
	print("enter rows > 0")
else:
	k=0
	p=0
	while(k<=str_len-1):
		while(p<row_len and k<str_len):
			#statement
			#print("l1:",k,p)
			row[p]=row[p]+inp[k]
			#print("loop1",row[p])
			p+=1
			k+=1
		p-=2
		while(p>=0 and k<str_len):
			#statement
			#print("l2:",k,p)
			row[p]=row[p]+inp[k]
			#print("loop2",row[p])
			p-=1
			k+=1
		p+=2
			
for i in row:
	output_String+=i

print(output_String)








