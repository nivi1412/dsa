#array8.py
#difference between max and min of array

inp=input("enter elements of array:")
Arr=list(map(int,inp.split()))

max_value=arr[0]
min_value=arr[0]

for i in range(len(Arr)):
	if(i>max_value):
		max_value=arr[i]
	if(i<min_value):
		min_value=arr[i]
print(max_value-min_value)
