#twosum.py

def twosum(Arr,num):
	p=0
	r=len(Arr)-1
	diff=(Arr[r]+Arr[p])
	closest = Arr[0] + Arr[1]
	while(p<r):
		if (abs(num - (Arr[p] + Arr[r])) < abs(num - closest)):
			closest = Arr[p] + Arr[r]
		if Arr[p]+Arr[r]==num:
			return Arr[p]+Arr[r]
		elif (Arr[p]+Arr[r] < num):
			p+=1
		elif (Arr[p]+Arr[r] > num):
			r-=1

	return closest		


	# if p==r and r!=(len(Arr)-1) and p!=0 :
	# 	diff1=abs((Arr[p-1]+Arr[r]) - num) 
	# 	diff2=abs((Arr[p]+Arr[r+1]) - num)

	# 	if(diff1<diff2):
	# 		return (Arr[p-1]+Arr[r])
	# 	else:
	# 		return (Arr[p]+Arr[r+1])
	# if (p==r and r==len(Arr)-1):
	# 	return Arr[p-1]+Arr[r]
	# if (p==r and p==0):
	# 	return Arr[p]+Arr[r+1]



inp=input("enter the array seperated by spaces:")
Arr=list(map(int,inp.split()))
num=int(input("enter the number:"))

tsum=twosum(Arr,num)
print(tsum)

