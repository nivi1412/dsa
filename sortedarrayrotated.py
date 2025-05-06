#given sorted array and it is rotated at a index x, find if y is in the array
#4 5 6 7 1 2 3 

import bisect


inp = input("enter the sorted array which is rotated spaces")
Arr = list(map(int,inp.split()))
index = int(input("enter the index at which its rotated: ")) #3
num = int(input("enter the number to be searched: "))

length = len(Arr)-1
maxindex = length-index
print(maxindex)
print(Arr[maxindex])
print(Arr[maxindex+1])


if (num > Arr[maxindex]) or (num < Arr[maxindex+1]):
	print("-1")

else:
	Arr1=Arr[0:maxindex+1]
	Arr2=Arr[maxindex+1:length+1]

	print(Arr1)
	print(Arr2)
	print(num)

	if Arr1[0]<=num<=Arr1[len(Arr1)-1]:
		ind1=bisect.bisect(Arr1,num)
		print("number is found at",ind1-1,"th index")
	elif Arr2[0]<=num<=Arr2[len(Arr2)-1]:
		ind2=bisect.bisect(Arr2,num)
		print("number is found at",(maxindex+ind2),"th index")






