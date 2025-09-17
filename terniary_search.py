#terniarysearch
#if the input increases reaches peak and decreases search the peak maximum

def terinarysearch(Arr):
	p=0
	r=len(Arr)-1

	while(p<r):
		q1=((2*p)+r)//3
		q2=(p+(2*r))//3
		print("p:",p)
		print("q1:",q1)
		print("q2:",q2)
		print("r:",r)
		if (r-p)<2:
			if(Arr[p]>Arr[r]):
				return p
			else:
				return r

		if(Arr[q1]>=Arr[p] and Arr[q2]>=Arr[q1] and Arr[r]>=Arr[q2]):
			p=q1+1
		elif(Arr[q1]>=Arr[p] and Arr[q2]>=Arr[q1] and Arr[r]<=Arr[q2]):
			p=q1+1
		elif (Arr[q1]>=Arr[p] and Arr[q2]<=Arr[q1] and Arr[r]<=Arr[q2]):
			r=q2-1
		elif (Arr[q1]<=Arr[p] and Arr[q2]<=Arr[q1] and Arr[r]<=Arr[q2]):
			r=q2-1
		else: pass
	

inp=input("enter the array value seperated by spaces")
Arr=list(map(int,inp.split()))                            
r=terinarysearch(Arr)
print(Arr[r])