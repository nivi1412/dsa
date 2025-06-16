#binarysearch3.py
#find the i,j pair such that A[i]+A[j]=B


def binarysearch(A,diff,p,r):
	q=(p+r)//2
	if A[q]==diff:
		return q
	elif p==r:
		return -1
	elif A[q]<diff:
		return binarysearch(A,diff,q+1,r)
	elif A[q]>diff:
		return binarysearch(A,diff,p,q)

def findpair(A,B):
	result=[]
	for i in range(len(A)):
		p=0
		r=len(A)-1
		j=binarysearch(A,(B-A[i]),p,r)
		if j!=-1 and j!=i:
			print("found pairs:",[A[i],A[j]])
	if j==-1:
		print("no pair found")


inp=input("enter the array sep by spaces:")
A=list(map(int,inp.split()))
B=int(input("req sum value :"))
findpair(A,B)

