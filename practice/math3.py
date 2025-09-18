#math3.py
#find number of trailing zeros for a factorial

num=int(input("enter the factorial whose trailing zeroes req:"))
count=0

while num//5>0:
	count=count+(num//5)
	num=num//5
print(count)
