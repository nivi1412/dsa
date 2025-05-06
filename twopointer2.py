#twopointer2.py
#print common numbers in given arrays

inp1=input("enter Array1 seperated by spaces:")
inp2=input("enter Array2 seperated by spaces:")
Arr1=list(map(int,inp1.split()))
Arr2=list(map(int,inp2.split()))

result=[]
i=0
j=0
k=max(len(Arr1),len(Arr2))
l=min(len(Arr1),len(Arr2))

if (len(Arr1)>=len(Arr2)):
	while (i<k):
		if (j<l):
			if Arr1[i]==Arr2[j]:
				result.append(Arr1[i])
				i+=1
				j+=1
			else:
				if(Arr1[i]<Arr2[j]):
					i+=1
				else:
					j+=1
		else:
			break
else:
	while(j<l):
		print("j,k:",j,k)
		if(i<k):
			print("i,l:",i,l)
			if(Arr1[j])==Arr2[i]:
				result.append(Arr1[j])
				i+=1
				j+=1
			else:
				print(Arr1[j])
				if(Arr1[j]<Arr2[i]):
					j+=1
				else:
					i+=1
		else:
			break

print(result)
