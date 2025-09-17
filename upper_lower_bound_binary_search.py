#searchelement and find the count of the number repeated in the array

def upperbound(Arr,num):
	p=0
	r=len(Arr)-1
	while p<=r:
		q=(p+r)//2
		if(Arr[q]>num):
			r=q-1
		else:
			p=q+1
	return r+1

def lowerbound(Arr,num):
	p=0
	r=len(Arr)-1
	while p<=r:
		q=(p+r)//2
		if(Arr[q]<num):
			p=q+1
		else:
			r=q-1
	return p

	

inp=input("enter the elements of an array seperated by spaces")
inp1=int(input("enter number to be searched"))
Arr=list(map(int,inp.split()))


count=upperbound(Arr,inp1)-lowerbound(Arr,inp1)
print(upperbound(Arr,inp1))
print(lowerbound(Arr,inp1))

print(count)