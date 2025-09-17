#given sorted array and given a number check if the number exists in the array findelementsortedaray.py
#python uses pass by reference so this algorithm is logn
def Search(Arr,num,p,r):
	

	num=num
	q=(r+p)//2
	#print("calc q:",q)


	if (Arr[q]>=num and (p!=r)):
		#print("left",q)
		Search(Arr,num,p,q)
	elif (Arr[q]<num and (p!=r)):
		#print("right:",q)
		Search(Arr,num,(q+1),r)
	elif (Arr[q]==num and p==r):
		print(q)
	else:
		print("-1")



inp=input("enter sorted array seperated by spaces")
Arr=list(map(int,inp.split()))
num=int(input("enter number to be searched:"))
r=len(Arr)-1
p=0

Search(Arr,num,p,r)

