#merge_2sortedarrays.py
#Merge two sorted arrays into a single sorted array

Arr1=input("enter the array seperated by spaces:")
Arr1=list(map(int,Arr1.split()))

Arr2=input("enter the array seperated by spaces:")
Arr2=list(map(int,Arr2.split()))

Arr=[]

i=0
j=0
k=0

while(i<len(Arr1) and j< len(Arr2)):
	if Arr1[i]<Arr2[j]:
		Arr.append(Arr1[i])
		i+=1
	else:
		Arr.append(Arr2[j])
		j+=1
while(i<len(Arr1)):
	Arr.append(Arr1[i])
	i+=1
while(j<len(Arr2)):
	Arr.append(Arr2[j])
	j+=1
print(Arr)