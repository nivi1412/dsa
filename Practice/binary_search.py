#binarysearch.py
#1.return if num is present or no
#2. return index of the num

def binarusearch(inp,num,p,r):
	q=(p+r)//2
	if inp[q]==num:
		return True,q
	elif p==r:
		return False,-1
	elif inp[q]>num:
		return binarusearch(inp,num,p,q)
	elif inp[q]<num:
		return binarusearch(inp,num,q+1,r)


inp=input("enter sorted list:")
inp=list(map(int,inp.split()))
num=int(input("enter number to be searched:"))
p=0
r=len(inp)-1
print(binarusearch(inp,num,p,r))