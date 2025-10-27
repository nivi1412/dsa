#dp_count_unique_digits.py
n=int(input("enter the integer: "))

total=10 if n>=1 else 1
unique=9
available=9

for i in range(2,n+1):
	unique*=available
	total+=unique
	available-=1

print(total)
