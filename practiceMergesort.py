#practiceMergesort.py

def Merge(p,q,r,Arr):
	len_left=q-p+1
	len_right=r-q
	Arr_left=[0 for i in range(len_left)]
	Arr_right=[0 for i in range(len_right)]

	for i in range(len_left):
		Arr_left[i]=Arr[p+i]
	for i in range(len_right):
		Arr_right[i]=Arr[q+1+i]

	i=0
	j=0
	k=p

	while i<len_left and j<len_right :
		if Arr_left[i]<Arr_right[j]:
			Arr[k]=Arr_left[i]
			i+=1
			k+=1
		else:
			Arr[k]=Arr_right[j]
			j+=1
			k+=1
	while(i<len_left):
		Arr[k]=Arr_left[i]
		i+=1
		k+=1
	while(j<len_right):
		Arr[k]=Arr_right[j]
		j+=1
		k+=1


def mergesort(p,r,Arr):
	if p>=r:
		return
	else:
		q=(p+r)//2
	mergesort(p,q,Arr)
	mergesort(q+1,r,Arr)
	Merge(p,q,r,Arr)



inp=input("enter the array to be sorted seperated by spaces:")
Arr=list(map(int,inp.split()))

p=0
r=len(Arr)-1
length=len(Arr)
sorted_Arr=mergesort(p,r,Arr)

print(Arr)