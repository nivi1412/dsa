#math6.py
#least of all the values greater than the num given

num=input("enter number:")
newnum=""
count=0
index=0
nextnum=0



for i in range(len(num)-1,0,-1):
	if (num[i]>num[i-1]):
		index=i-1
		break
	else:
		count+=1
if count!=len(num)-1:
	print(index)
	nextnum=num[index]
	for i in range(index):
		newnum=newnum+num[i]

	num=list(num[index:])
	print(num)
	print(newnum)
	num.sort()

	for i in range(len(num)-1):
		if (num[i]==nextnum):
			nextnum=num[i+1]
			break
	newnum=newnum+nextnum
	num.remove(nextnum)
	num.sort()
	for i in num:
		newnum=newnum+i

	print(num)
	print(newnum)
else:
	print("-1")


