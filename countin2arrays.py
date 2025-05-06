array1 = input('enter elements of array seperated by space')
array2 = input('enter elements of array seperated by space')
array1 = array1.split()
array2 = array2.split()
uniquecount=0
repeatcount=0

for i in array1:
	if i not in array2:
		repeatcount+=1

print("nuber of repeated elements :",repeatcount)


