#remove.py

inp=input("enter Array seperated by spaces:")
Arr=list(map(int,inp.split()))
i=0
while(i<len(Arr)):

	if i==0:
		i+=1
	else:
		if Arr[i-1] == Arr[i]:
			Arr.pop(i)
		else:
			i+=1
print(Arr)


