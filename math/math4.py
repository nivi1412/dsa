#math4.py
#revesed the integer

# num=input("enter the number:")
# l=len(num)-1
# newnum=""
# for i in range(len(num)-1,-1,-1):
# 	if ("-" in num) and ("-" not in newnum):
# 		newnum=newnum+"-"+num[i]
# 	else:
# 		newnum=newnum+num[i]
# if ("-" in newnum):
# 	print(newnum[0:len(newnum)-1])
# else:
# 	print(newnum)

#consider number is a integer

def refactor(num):
	newnum=[]
	finalnum=0
	while(num>0):
		rem=num%10
		num=num//10
		newnum.append(rem)
	l=len(newnum)
	j=0
	for i in range(l-1,-1,-1):
		finalnum=finalnum+(10**i)*newnum[j]
		j+=1
	return finalnum


num=input("enter the number:")
num=int(num)
if num>0:
	finalnum=refactor(num)
	print(finalnum)
else:
	num=num*-1
	finalnum=refactor(num)
	print(finalnum*-1)











