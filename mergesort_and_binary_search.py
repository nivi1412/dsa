#a[i]+b[j]=c.py
#MSandBS.py

def Merge(Arr,p,q,r):
	nl=q-p+1
	nr=r-q
	left=Arr[p:q+1]
	right=Arr[q+1:r+1]

	i=0
	j=0
	k=p

	while(i<nl and j<nr):
		if(left[i]<=right[j]):
			Arr[k]=left[i]
			i=i+1
			k=k+1
		else:
			Arr[k]=right[j]
			j=j+1
			k=k+1

	while(i<nl):
		Arr[k]=left[i]
		k=k+1
		i=i+1
	while(j<nr):
		Arr[k]=right[j]
		k=k+1
		j=j+1



def Mergesort(Arr,p,r):

	if(p<r):
		q=(p+r)//2
	else :
		return
	Mergesort(Arr,p,q)
	Mergesort(Arr,q+1,r)
	Merge(Arr,p,q,r)

def Binarysearch(B,p,r,element):
	q=(p+r)//2
	if (B[q]>=element and (p!=r)):
		return Binarysearch(B,p,q,element)
	elif(B[q]<element and (p!=r)):
		return Binarysearch(B,q+1,r,element)
	elif(B[q]==element and p==r):
		return q
	else:
		return -1



inp1=input("enter elements of 1st array with spaces")
inp2=input("enter elements of 2nd array with spaces")
num=int(input("enter the sum number:"))

A=list(map(int,inp1.split()))
B=list(map(int,inp2.split()))

p=0
len1=len(A)
len2=len(B)

Mergesort(A,p,len1-1)
Mergesort(B,p,len2-1)

#find i,j pair such that A[i]+B[j]=C

for i in range(len(A)):
	element=num-A[i]
	p=0
	r=len(B)-1
	j=Binarysearch(B,p,r,element)
	print(A[i])
	print(B[j])

