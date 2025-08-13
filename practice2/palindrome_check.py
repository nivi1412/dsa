#palindrome_check.py
#Check if an array is a palindrome

Arr=input("enter the array seperated by spaces:")
Arr=list(map(int,Arr.split()))

p=0
r=len(Arr)-1
is_palindrom=True

while True:
	if p>=r:
		break
	if Arr[p]==Arr[r]:
		p+=1
		r-=1
	else:
		is_palindrom=False
		break

if is_palindrom:
	print("palindrome")
else:
	print("not a palindrome")