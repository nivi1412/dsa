#remove_duplicates_Array.py
#Remove duplicates from a sorted array

Arr=input("enter the array seperated by spaces:")
Arr=list(map(int,Arr.split()))

p=1
r=0

while p<len(Arr):
	if Arr[p]==Arr[r]:
		Arr.remove(Arr[r])
	else:
		p+=1
		r+=1
print(Arr)
	
		