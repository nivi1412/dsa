#mergesort.py

def merge(inp,p,q,r):
	nl=q-p+1 
	nr=r-q
	left_arr=[0]*nl
	right_arr=[0 for _ in range(nr)]

	for i in range(len(left_arr)):
		left_arr[i]=inp[p+i] #point3
	for j in range(len(right_arr)):
		right_arr[j]=inp[q+j+1] #point4

	i=0
	j=0
	k=p    #point1

	while i<nl and j<nr:  #point2
		if left_arr[i]<right_arr[j]:
			inp[k]=left_arr[i]
			i+=1
			k+=1
		else:
			inp[k]=right_arr[j]
			j+=1
			k+=1
	while i<nl:
		inp[k]=left_arr[i]
		i+=1
		k+=1
	while j<nr:
		inp[k]=right_arr[j]
		j+=1
		k+=1

def mergesort(inp,p,r):
	if (p>=r):  #point5
		return
	else:
		q=(p+r)//2
		mergesort(inp,p,q)
		mergesort(inp,q+1,r)
		merge(inp,p,q,r)

inp=list(map(int,input("enter thr array to be sorted seperated by spaces:").split()))
p=0
r=len(inp)-1
mergesort(inp,p,r)
print(inp)