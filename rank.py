#find rank of the given string
import math

DIV = 1000003

def rank(Arr,org_Arr):
	i=0
	j=0
	rank=0
	while(j<len(Arr)):
		if org_Arr[i]==Arr[j]:
			Arr.remove(Arr[j])
			org_Arr.remove(org_Arr[i])
			j=0

		else:
			rank=(rank+(math.factorial(len(org_Arr)-1) % DIV)) % DIV
			j+=1
	return rank+1

inp=input("enter the string seperated by spaces")
Arr=inp.split()
org_Arr=Arr.copy()
Arr.sort()
rank=rank(Arr,org_Arr)

print(rank % DIV)
