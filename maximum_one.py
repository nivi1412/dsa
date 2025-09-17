#maximumone.py
#twopointer problem
#find maximum 1s by changing 0 to 1 in binary (b count's of 0s to 1)

# Mistakes: Mixed up conditions in while and if

def twopointer(Arr,num):
	p=0
	r=p
	convert=0
	prev_count=0
	while(r<=len(Arr)-1):

		while(convert<num and r<=len(Arr)-1):
			if Arr[r]==0:
				convert+=1
				r+=1
			else:
				r+=1

		while(convert==num and r<=len(Arr)-1 and Arr[r]==1):
			r+=1
		print("p,r:",p,r)
		if(r-p > prev_count): 
			prev_count=r-p
			# return prev_count

		if(Arr[p]==0 ):
			convert-=1
			p+=1
		elif(Arr[p]==1):
			p+=1


	return prev_count

inp=input("enter the binary array seperated by spaces:")
Arr=list(map(int,inp.split()))
num=int(input("enter the number od 0's to be converted to 1:"))

maximum= twopointer(Arr,num)
print(maximum)