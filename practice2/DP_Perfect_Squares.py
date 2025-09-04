# DP_Perfect_Squares.py
import math

def perfectsquares(n,count)->int: #count return 
	if n==1:
		return 1
	if n==2:
		return 2
	if n==3:
		return 3
	else:
		num=math.isqrt(n)
		for i in range(num,0,-1):
			rem = n-(i*i)
			count+=1 #(since i*i is first num)
			if rem!=0:
				if perfectsquares(rem,count)>0:
					count+=perfectsquares(rem,count)
				else:
					count=0
			else: return count
		return count

n=int(input("enter the num: "))
print(perfectsquares(n,count=0))


