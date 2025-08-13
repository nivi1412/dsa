#Inplace_Array_reversal.py
#Reverse an array in-place

Arr=input("enter the array seperated by spaces:")
Arr=list(map(int,Arr.split()))

p=0
r=len(Arr)-1

while True:
	if p>=r:
		break
	Arr[p],Arr[r]=Arr[r],Arr[p]
	p+=1
	r-=1
print(Arr)