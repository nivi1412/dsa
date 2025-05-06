#threesum.py
#return 3 digits Sum whose sum is near to given number - num

def threesum(Arr,num):
	closest=Arr[0]+Arr[1]+Arr[2]
	for i in range(0,len(Arr)-2,+1):
		j=i+1
		k=len(Arr)-1
		while(j<k):
			if(abs(Arr[i]+Arr[j]+Arr[k] - num) < abs(closest - num)):
				closest=abs(Arr[i]+Arr[j]+Arr[k])
			if (Arr[i]+Arr[j]+Arr[k]) == num:
				closest = Arr[i]+Arr[j]+Arr[k]
			elif (Arr[i]+Arr[j]+Arr[k]) < num:
				j+=1
			else:
				k-=1

			# if j==k and j!=i+1 and k!=len(Arr)-1 :
			# 	diff1=abs(Arr[i]+Arr[j]+Arr[k]-num)

			# 	if diff1 <  abs(diff-num):
			# 		diff=Arr[i]+Arr[j]+Arr[k]

			# if j==k and j==i+1 :
			# 	diff1=abs(Arr[i]+Arr[j]+Arr[k+1]-num)

			# 	if diff1 <  abs(diff-num):
			# 		diff=Arr[i]+Arr[j]+Arr[k+1]


			# if j==k and k==len(Arr)-1 :
			# 	diff1=abs(Arr[i]+Arr[j-1]+Arr[k]-num)

			# 	if diff1 <  abs(diff-num):
			# 		diff=Arr[i]+Arr[j-1]+Arr[k]

	return closest

inp=input("enter the array seperated by spaces:")
Arr=list(map(int,inp.split()))
num=int(input("enter the number:"))
summ=threesum(Arr,num)

print(summ)

	



