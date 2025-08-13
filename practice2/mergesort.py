#mergesort.py
#Timecomplexity O(n*logn)

def merge(Arr,p,q,r):

	nl=q-p+1
	nr=r-q

	Arr_left=[0]*nl
	Arr_right=[0]*nr

	for i in range(nl):
		Arr_left[i]=Arr[p+i]
	for j in range(nr):
		Arr_right[j]=Arr[q+j+1]
	

	i=0
	j=0
	k=p

	while(i<nl and j<nr):
		if Arr_left[i]<Arr_right[j]:
			Arr[k]=Arr_left[i]
			i+=1
			k+=1
		else:
			Arr[k]=Arr_right[j]
			j+=1
			k+=1

	while(i<nl):
		Arr[k]=Arr_left[i]
		i+=1
		k+=1

	while(j<nr):
		Arr[k]=Arr_right[j]
		j+=1
		k+=1


def mergesort(Arr,p,r):
	if p>=r:
		return
	q=(p+r)//2
	mergesort(Arr,p,q)
	mergesort(Arr,q+1,r)
	merge(Arr,p,q,r)

Arr=input("enter the elements of array to be sorted:")
Arr=list(map(int,Arr.split()))

p=0
r=len(Arr)-1

mergesort(Arr,p,r)
print(Arr)