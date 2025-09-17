#calculate prefix sum array calculateprefixsumarray.py

arr=input('input numbers in array followed by spaces')
arr=arr.split()
arr=[int(i) for i in arr]

p=[0]*len(arr)

p[0]=arr[0]

i=1
while i<len(arr):
	p[i]=p[i-1]+arr[i]
	i+=1

print("prefix array:")
for i in range(len(p)):
	print(p[i])
	

