# DP_Perfect_Squares.py
import math
import pdb

def perfectsquares(n,count,dp)->int: #count return 
	if n in dp:
		return dp[n]
	my_list=[]
	num=math.isqrt(n)
	# print("num:",num)
	for i in range(num,0,-1):
		# pdb.set_trace()
		# print("n,count",n,count)
		rem = n-(i*i)
		count=1 #(since i*i is first num)
		if rem==0:
			pass
		elif 0 < rem <=3:
			count+=rem
		elif rem > 3:
			count+=perfectsquares(rem,count,dp)
		else:
			count=0
		my_list.append(count)
	dp[n]=min(my_list)
	return min(my_list)


n=int(input("enter the num: "))
dp={}
print(perfectsquares(n,0,dp))


