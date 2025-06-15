#binarysearch2.py

#given sorted array and it is rotated at a index x, find if y is in the array and find x as well
#4 5 6 7 1 2 3 

def findpivotindex(Arr,p,r):
	q=(p+r)//2
	if q!=p or q!=r:
		if Arr[q]>=Arr[p] and Arr[q]>=Arr[r]:
			if Arr[q+1]>Arr[r]:
				return findpivotindex(Arr,q,r)
			else:
				return q
		elif Arr[q]>=Arr[p] and Arr[q]<=Arr[r]:
			print("full-increasing", p,q,r)
			print("full-increasing", Arr[p],Arr[q],Arr[r])
			return 0
		elif Arr[q]<=Arr[p] and Arr[q]<=Arr[r]:
			return findpivotindex(Arr,p,q)
		elif Arr[q]<Arr[p]  and Arr[q]>Arr[r]:
			return findpivotindex(Arr,q,r)
	elif q==p:
		if Arr[p]>Arr[r]:
			return p
		else:
			return -1
	elif q==r:
			print("no-case", p,q,r)
			print("no-case-values", Arr[p],Arr[q],Arr[r])

def binarysearch(Arr,ele,p,r):
	q=(p+r)//2
	print(p,q,r)
	print(Arr[q],"==",ele)
	if Arr[q]==ele:
		return True
	elif p==r:
		return False
	elif Arr[q]>ele:
		return binarysearch(Arr,ele,p,q)
	elif Arr[q]<ele:
		return binarysearch(Arr,ele,q+1,r)


inp=input("enter the array sep by spaces:")
inp=list(map(int,inp.split()))
#index=int(input("enter the index at which array is pivoted:"))
ele=int(input("enter the element to be searched:"))
p=0
r=len(inp)-1
index=findpivotindex(inp,p,r)
print("index of pivot",index)
if index ==-1:
	Arr2=inp[:len(inp)]
	print(Arr2)
	Arr1=[]
else:
	Arr1=inp[index+1:]
	Arr2=inp[:index+1]
print(Arr1)
print(Arr2)
p1=0
r1=len(Arr1)-1
p2=0
r2=len(Arr2)-1

is_true=binarysearch(Arr1,ele,p1,r1)
if not(is_true):
	print(binarysearch(Arr2,ele,p2,r2))
else:
	print(is_true)


