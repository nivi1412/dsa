#math1.py
#find if number is prime or not
import math
inp=int(input("enter the number"))
flag=True
if inp <2:
	print("neither prime nor composite")
elif inp==2 or inp==3:
	print("prime")
else:
	for i in range(2,int(math.sqrt(inp))+1,+1):
		if inp%i==0:
			print("not a prime")
			flag=False
			break
	if flag:
		print("prime")