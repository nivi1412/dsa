#math2.py
#reverse integer

num=input("enter teh num to be reversed:")
newnum=0
num_len=len(num)
num=int(num)

for i in range(num_len-1,-1,-1):
	rem=num%10
	newnum=newnum+rem*(10**i)
	num=num//10
print(newnum)

