#math5.py
#print trailing zeros 

num=int(input("enter positive number"))

i=5
count=0

while((num//i)!=0):
	count=count+(num//i)
	i=i*5
print("trailing zeros:",count)


