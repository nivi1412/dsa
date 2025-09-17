inp=input("enter the array seperated by spaces:")
Arr=list(map(int,inp.split()))
num=int(input("enter the number:"))

diff=[]
left_diff=[]
right_diff=[]
closest = Arr[0] + Arr[1] + Arr[2]
closest_i=0
closest_j=1
closest_k=2
for i in range(len(Arr)):
	for j in range(i+1,len(Arr),+1):
		for k in range(j+1,len(Arr),+1):

			three_sum=Arr[i]+Arr[j]+Arr[k]
			if (abs(three_sum - num) < abs(closest - num)):
				closest = three_sum
				closest_i=i
				closest_j=j
				closest_k=k

print(closest)
print(closest_i,closest_j,closest_k)
