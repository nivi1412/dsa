#merge ( sort & combine)

def Merge(Arr,p,q,r):
	#length of left and right arrays and make left and right arrays
	nl=q-p+1
	nr=r-q
	left=[0]*nl
	right=[0]*nr

	for i in range(nl):
		left[i]=Arr[p+i]
	for i in range(nr):
		right[i]=Arr[q+1+i]

	#sort and combine 
	i=0
	j=0
	k=p 

	while(i<nl and j<nr):
		if left[i]>right[j]:
			Arr[k]=right[j]
			k+=1
			j+=1
		else:
			Arr[k]=left[i]
			i+=1
			k+=1

	while(i<nl):
		Arr[k]=left[i]
		i+=1
		k+=1
	while(j<nr):
		Arr[k]=right[j]
		j+=1
		k+=1


#mergesort (divide)
def Mergesort(Arr,p,r):
	if p>=r:
		return
	else:
		q=(p+r)//2
	Mergesort(Arr,p,q)
	Mergesort(Arr,q+1,r)
	Merge(Arr,p,q,r)


#enter the array to be sorted

inp=input("enter elements of array needs to be sorted seperated by spaces:")
inp=list(map(int, inp.split()))
Arr=inp
p=0
r=len(Arr)-1
Mergesort(Arr,p,r)

print("sorted array :")
for i in Arr:
	print(i)