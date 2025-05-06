#given sorted array and it is rotated at a index x, find if y is in the array and find x as well
#4 5 6 7 1 2 3 

import bisect

def binarysearch(Arr,p,r):
   if(p!=r):
   		q=(p+r)//2
   		if(q!=p and q!=r):
   			if(Arr[q]>Arr[q-1] and Arr[q]>Arr[q+1]):
   				return q	
   			elif(Arr[q]<Arr[q-1] and Arr[q]<Arr[q+1] and Arr[q-1]>Arr[q+1]):
   				return q-1
   			elif(Arr[q]<Arr[q+1] and Arr[q]>Arr[q-1]):
   				if Arr[q]<Arr[p]:
   					r=q-1
   					return binarysearch(Arr,p,r)
   				else:
   					p=q+1
   					return binarysearch(Arr,p,r)
   			elif(Arr[q]<Arr[q+1] and Arr[q]>Arr[q-1] and Arr[q]>Arr[r]):
   				p=q+1
   				return binarysearch(Arr,p,r)
   			else:
   				print("oops u missed a condition")
   		elif(q==p and Arr[p]>Arr[r]):
   			return q
   		elif(q==p and Arr[p]<Arr[r]):
   			return r
   if p==r:
   	return p
		

inp = input("enter the sorted array which is rotated spaces")
Arr = list(map(int,inp.split()))
#index = int(input("enter the index at which its rotated: ")) #3
num = int(input("enter the number to be searched: "))
#find index

p=0
r=len(Arr)-1
index=binarysearch(Arr,p,r)
print("index",index)
length = len(Arr)-1
maxindex = index


if (num > Arr[maxindex]):
	print("-1")

else:
	Arr1=Arr[0:maxindex+1]
	Arr2=Arr[maxindex+1:length+1]

	print(Arr1)
	print(Arr2)
	print(num)

	if Arr1[0]<=num<=Arr1[len(Arr1)-1]:
		ind1=bisect.bisect(Arr1,num)
		print("number is found at",ind1-1,"th index and array is rotated at index:",index)
	elif Arr2[0]<=num<=Arr2[len(Arr2)-1]:
		ind2=bisect.bisect(Arr2,num)
		print("number is found at",(maxindex+ind2),"th index and array is rotated at index:",index)






