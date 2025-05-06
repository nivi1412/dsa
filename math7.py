#math7.py
#decimal to binary

num=int(input("enter the number:"))
rem=[]
while num>0:
	rem.append(num%2)
	num=num//2
print(rem)
l=len(rem)
binary=0
for i in range(l):
	print(i)
	binary=binary+rem[i]*(10**i)
print(binary)



