#fibonocci.py (timecomplexity + code practice)
#time complexity O(n)

memo={}
def fibonacci(n,arr):

	if n<=1:
		return n
	elif n in memo:
		return memo[n]
	else:
		memo[n]=fibonacci(n-1,arr)+fibonacci(n-2,arr)
		arr.append(memo[n])
		return memo[n]

arr=[]
n=int(input("enter the range of fibonocci series to be displayed:"))
fibonacci(n,arr)

print(arr)