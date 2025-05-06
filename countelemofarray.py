#countelementsofarrayrepeatedand non repeated

arr=input("enter elementa seperated by spaces")
arr=arr.split()
arr= [int(i) for i in arr]

my_dict={}

for i in arr:
	if i in my_dict:
		my_dict[i]+=1
	else:
		my_dict[i]=1
for key, value in my_dict.items():
	print("key ",key,  ":",value)


