#difference between max and min of array

inp=input("enter elements of array seperated by spaces:")

arr=list(map(int,inp.split()))

maxx=max(arr)
minn=min(arr)

print(maxx-minn)

#without builtion functions
max_value=arr[0]
min_value=arr[0]


for i in range(len(arr)):
	if(i>max_value):
		max_value=arr[i]
	if(i<min_value):
		min_value=arr[i]
print(max_value-min_value)
