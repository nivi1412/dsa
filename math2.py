#math2.py
#find all prime numbers till given num

#O(n**3/2)

# def prime(num):
# 	count=0
# 	if num >=2:
# 		for i in range(2,num):
# 			if num%i==0:
# 				count+=1
# 		if count!=0:
# 			return False
# 		else:
# 			return True

# num=int(input("enter a positive number:"))
# Array=[]
# if num > 2:
# 	for i in range(2,num+1):
# 		flag=prime(i)
# 		if flag==True:
# 			Array.append(i)
# 	print(Array)
# else:
# 	print("number is invalid")

#O(nlog logn)
num=int(input("enter range of prime numbers to be printed:"))
Arr=[i for i in range(2,num+1)]
lArr=len(Arr)
pArr=[True for i in range(2,num+1)]
# print(Arr)
# print(pArr)

for i in range(len(pArr)):
	#print("i",i)
	if pArr[i]==True:
		for j in range(Arr[i]+i,lArr,+Arr[i]):
			#print(Arr[j])
			pArr[j]=False
for i in range(len(pArr)):
	if pArr[i]:
		print(Arr[i])

# print(Arr)
# print(pArr)



