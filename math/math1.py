#math1.py
#find if number is prime or not

import math
num=int(input("enter a positive number:"))
count=0
if(num <2):
	print("enter valid number >=2")
if num==2 or num==3:
	print("its a primenumber")
if num >2:
	for i in range(2,int(math.sqrt(num))+1):
		if num%i==0:
			print("not a prime")
			count=0
			break
		else:
			count+=1
	if count!=0:
		print("its a primenumber")
