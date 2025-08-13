#binarysearch.py
#timecomplexity: nlogn

def binarysearch(Arr,p,r,n):
	if p>=r:
		return(-1)
	else:
		q=(p+r)//2
		if Arr[q]==n:
			return q
		elif Arr[q]>n:
			return binarysearch(Arr,p,q,n)
		elif Arr[q]<n:
			return binarysearch(Arr,q+1,r,n)

Arr=input("enter the sorted arrray :")
Arr=list(map(int,Arr.split()))
n=int(input("enter element to be searched:"))
p=0
r=len(Arr)-1

q=binarysearch(Arr,p,r,n)
if q==-1:
	print("no not in array")
else:
	print("number in the array is at index",q)
