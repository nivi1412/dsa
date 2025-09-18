#Heap sort
def Heapify(Arr,n,i):
	largest=i

	left = 2*i+1
	right = 2*i+2

	if(left<n and Arr[left]>Arr[largest]):
		largest=left
	if(right<n and Arr[right]>Arr[largest]):
		largest=right
	if (largest!=i):
		Arr[i],Arr[largest]=Arr[largest],Arr[i]
		Heapify(Arr,n,largest)

def HeapSort(Arr):
	n=len(Arr)
	for i in range((n//2)-1,-1,-1):
		Heapify(Arr,n,i)

	for i in range(n-1,0,-1):
		Arr[i],Arr[0]=Arr[0],Arr[i]
		Heapify(Arr,i,0)


inp=input("enter the elements of array seperated by spaces:")
Arr=list(map(int,inp.split()))

HeapSort(Arr)

print("sorted array:")
for i in Arr:
	print(i)
