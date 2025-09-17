#practicebinarysearch.py
def Binarysearch(A,B):
	p=0
	r=len(A)-1



	while(1):
		q=(p+r)//2
		print(A[q],p,q,r)
		if p==r and A[q]!=B:
			return False
		elif A[q]==B:
			return True
		elif A[q]>B:
			r=q
		elif A[q]<B:
			p=q

inp=input("enter the sorted array seperated by spaces:")
A=list(map(int,inp.split()))
B=int(input("enter the number to be searched"))
print(Binarysearch(A,B))
