#count at what height do we need to strike a tree to cut the wood of reqired number
#[3 2 1 5 6 4] if we cut at height 6 we get 0 wood , at height 5 we get 1 wood 
#at height 4 we get 2 wood ..... findwoodheight.py

#bruteforce: make the descending order at keep pointer at position 1 
#at height i we get the count of wood by subtracting with the previous values

def Merge(Arr,p,q,r):
	left=Arr[p:q+1]
	right=Arr[q+1:r+1]

	i=0
	j=0
	k=p

	while(i<len(left) and j<len(right)):

		if(left[i]>right[j]):
			Arr[k]=left[i]
			i+=1
			k+=1
		else:
			Arr[k]=right[j]
			j+=1
			k+=1

	while(i<len(left)):
		Arr[k]=left[i]
		i+=1
		k+=1

	while(j<len(right)):
		Arr[k]=right[j]
		j+=1
		k+=1


def Mergesort(Arr,p,r):
	if(p<r):
		q=(p+r)//2
	else:
		return
	Mergesort(Arr,p,q)
	Mergesort(Arr,q+1,r)
	Merge(Arr,p,q,r)

def woodheight(Arr,woodcount):
	for i in range(0,len(Arr),+1):
		count=0
		for j in range(0,i,+1):
			count=count+(Arr[j]-Arr[i])	
		print(count)
		if count == woodcount:
			print("for wood count ", woodcount,"woodheight that needs to be cut at is:",Arr[i])
			return



inp=input("enter the wood rows seperated by spaces")
woodcount=int(input("enter the required wood count"))
Arr=list(map(int,inp.split()))

p=0
r=len(Arr)-1
Mergesort(Arr,p,r)
woodheight(Arr,woodcount)

		

