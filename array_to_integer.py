#convert 1 and 0 in an array into a decimal number

arr=input("enter 0's and 1's seperated by spaces with max length 30:")
arr=list(map(int,arr.split()))
arr1=[0]*len(arr)

i=0
j=len(arr)-1

while(i<len(arr)):
		arr1[i]=arr[j]
		i+=1
		j-=1

print(arr)
print(arr1)


integer=0
for i in range(len(arr1)):
	if len(arr1)<=30:
		integer=integer+(2**i * arr1[i])
	else:
		print("enter binary array length less than 30")
	

print("interger number:", integer)
