#test.py
#Aim: find the given num is a perfect is square
#list=['aba',"aaa","acb"]
#list=[true , true, false]

def if_palindrome(string):
	str_length= len(string)//2
	i=0
	j=len(string)-1
	is_pal=True

	while(i<=str_length):
		if string[i]==string[j]:
			i+=1
			j-=1
		else:
			is_pal=False
			break
	return is_pal


my_list=[]
final_out=[]
n=int(input("enter the length of string: "))

for i in range(n):
	string=input("enter the string")
	my_list.append(string)

for string in my_list:
	final_out.append(if_palindrome(string))

print(my_list)
print(final_out)