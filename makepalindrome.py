#makepalindrome.py

inp=input("enter the string:")
str_len=len(inp)
flag=True
if str_len%2 ==0:
	loop=str_len//2
else:
	loop=(str_len//2)+1

if str_len==0:
	print("string is empty")
elif str_len==1:
	print(0)
elif(str_len == 2):
	print(1)
else:
	p=0
	r=str_len-1
	k=0
	while(k<=loop-1):
		if(inp[p]==inp[r]):
			p+=1
			r-=1
			k+=1
		elif(inp[p]!=inp[r] and flag==True):
			if(inp[p+1]==inp[r]):
				p+=2
				r-=1
				flag=False
				k+=1
			elif(inp[p]==inp[r-1]):
				r-=2
				p+=1
				flag=False
				k+=1
			else:
				print(0)
				break
		elif(inp[p]!=inp[r] and flag==False):
			print(0)
			break
	if(k>(loop-1)):
		print(1)













