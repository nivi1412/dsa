#math5.py
#no of ways to reach from top left to bottom right corner for a m*n grid
def factorial(num):
	if num==0 or num==1:
		return 1
	elif num > 1:
		return (factorial(num-1)*(num))


m=int(input("enter no of rows:"))
n=int(input("enter no of cols:"))
m=m-1
n=n-1
total_moves=m+n

print("no of ways to arrange is:")

print(factorial(total_moves)//(factorial(total_moves-m) * factorial(m)))




