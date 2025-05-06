#find the i,j pair such that A[i]+A[j]=B

arr=list(map(int,input('enter input array seperated by spaces').split()))
b= int(input('enter required sum : '))


ans=[]

i=0
j=len(arr)-1
while i<len(arr)-1 :
	while j>i:
		if((arr[i]+arr[j])==b):
			ans.append((arr[i],arr[j]))
		j-=1
	i+=1
	j=len(arr)-1

print(ans)


