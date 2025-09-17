#terniarysearch.py
#if the input increases reaches peak and decreases search the peak maximum

def teriniarysearch(Arr,p,r):

	while(p<r):
		if (r-p)<2:
			if Arr[r]>Arr[p]:
				return Arr[r]
			else:
				return Arr[p]
		q1=(p+r)//3
		q2=2*(p+r)//3
		Arr1=Arr[p:q1]
		Arr2=Arr[q1:q2]
		Arr3=Arr[q2:r+1]



		if Arr[q1]>=Arr[p] and Arr[q2]>=Arr[q1] and Arr[r]<=Arr[q2]:
			p=q1+1
		elif Arr[q1]>=Arr[p] and Arr[q2]<=Arr[q1] and Arr[r]<=Arr[q2]:
			r=q2-1
		elif Arr[q1]<=Arr[p] and Arr[q2]<=Arr[q1] and Arr[r]<=Arr[q2]:
			r=q2-1
		elif Arr[q1]>=Arr[p] and Arr[q2]>=Arr[q1] and Arr[r]>=Arr[q2]:
			p=q1+1



Arr=input("enter the Array with increasing peak:")
Arr=list(map(int,Arr.split()))

p=0
r=len(Arr)-1
print(teriniarysearch(Arr,p,r))
