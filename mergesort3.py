#merge sort

def merge(arr,p,q,r):
	llen=int(q-p+1)
	rlen=int(r-q)

	larr=[0]*llen
	rarr=[0]*rlen 
	k=0

	for i in range(llen):
		larr[i]=int(arr[p+i])
	for j in range(rlen):
		rarr[j]=int(arr[q+1+j])

	i=0
	j=0
	k=p

	while (i<llen and j<rlen):
		if larr[i] < rarr[j]:
			arr[k]=larr[i]
			i+=1
			k+=1
		else:
			arr[k]=rarr[j]
			j+=1
			k+=1

	while i<llen:
		arr[k]=larr[i]
		k+=1
		i+=1
	while j<rlen:
		arr[k]=rarr[j]
		k+=1
		j+=1



def mergesort(arr,p,r):
	if r<=p:
		return
	else:
		q=(p+r)//2
	mergesort(arr,p,q)
	mergesort(arr,q+1,r)
	merge(arr,p,q,r)


arr=input("eneter input array to be sorted with space")
arr=arr.split()

arrlen=len(arr)
p=0
r=arrlen-1
mergesort(arr,p,r)

for i in range(len(arr)):
	print("sorted array:", arr[i])
