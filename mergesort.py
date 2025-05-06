def Merge(arr,p,q,r):
	nl=q-p+1; nr=r-q;

	left=[0]*nl
	right=[0]*nr
	print(p,q,r,nl-1,nr-1)
	for i in range(nl):
		left[i]=arr[p+i]
	for j in range(nr):
		right[j]=arr[q+j+1]
	i=0;j=0;k=p

	while i < nl and j < nr:
		if left[i] < right[j]:
			arr[k] = left[i]
			i += 1¬l¬
			k += 1
		else:
			arr[k] = right[j]
			j += 1
			k += 1
	while i < nl:
		arr[k]=left[i]
		k=k+1
		i=i+1
	while j < nr:
		arr[k]=right[j]
		k=k+1
		j=j+1

def Mergesort(arr,p,r):
	if(p>=r):
		return
	else:
	    q=(p+r)//2;
	print(p,r)
	Mergesort(arr,p,q)
	Mergesort(arr,q+1,r)
	Merge(arr,p,q,r)


arr = [60, 50, 40, 30, 20, 10, 30];
p=0;r=len(arr)-1;
print(len(arr))
sortedarray = Mergesort(arr,p,r);
print("sorted array:", arr)