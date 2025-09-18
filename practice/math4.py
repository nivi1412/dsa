#math4.py
#find the next lexicographical permutation of the digits of a number
# Given a positive integer as a string input, write a program to find the next greater number that can be formed using the same digits 
# of the input number. If no such number exists (i.e., the input is the largest possible permutation), output -1


num=int(input("enter the number:"))
num=str(num)
finalnum=''
for i in range(len(num)-2,-1,-1):
	if num[i]<num[i+1]:
		index1=i+1
		break
	else:
		print(-1)
		exit()
local=num[index1]
sub_num=num[:index1]
Min=10**5
for i in range(len(sub_num)):
	print(sub_num[i],Min,local)
	if sub_num[i]Min and sub_num[i]>local:
		Min=sub_num[i]
		index2=i
num=list(num)
num[index1],num[index1+index2+1]=num[index1+index2+1],num[index1]
first=num[:index1+1]
last=num[index1+1:]
last=sorted(last)
num=first+last
for i in num:
	finalnum=finalnum+i
print(finalnum)
