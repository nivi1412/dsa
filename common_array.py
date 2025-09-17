#intersection of 2 arrays sortes
def commonarray(Arr1,Arr2,i,j,k,l):
	result=[]
	while (i<k and j<l):
			if Arr1[i]==Arr2[j]:
				result.append(Arr1[i])
				i+=1
				j+=1
			else:
				if(Arr1[i]<Arr2[j]):
					i+=1
				else:
					j+=1

	return result




inp1=input("enter Array1 seperated by spaces:")
inp2=input("enter Array2 seperated by spaces:")
Arr1=list(map(int,inp1.split()))
Arr2=list(map(int,inp2.split()))

i=0
j=0
k=len(Arr1)
l=len(Arr2)

if (len(Arr1)>=len(Arr2)):
	res=commonarray(Arr1,Arr2,i,j,k,l)
else:
	res=commonarray(Arr2,Arr1,i,j,l,k)

if (len(res)!=0):
	print(res)
	print("max:",max(res))
else:
	print(res)


