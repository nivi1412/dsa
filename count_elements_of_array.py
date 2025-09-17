#count no of elements in the array 

elements = input('enter elements of array seperated by space')
elements = elements.split()
count=0
for i in elements:
	count=count+1
print("number of elements in array:",count)
#number of unique elements in the array
unique_elements=[]
for i in elements:
	if i not in unique_elements:
		unique_elements.append(i)
unique_count=0
for i in unique_elements:
	unique_count=unique_count+1
print('number of unique elements :', unique_count)

#count of each number in the array
count1 = [0]*unique_count
print(count1)
k=0
for i in unique_elements:
	print("unique_elements:",i)
	for j in elements:
		print(j)
		if(i==j):
			count1[k]=count1[k]+1

	k+=1

for i in range(unique_count):
	print("number of ", unique_elements[i] ,"'s:" , int(count1[i]))
#number of distinct elements and unique element







	
    


