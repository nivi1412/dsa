# DP_Ugly_Number_II.py

def is_ugly(i,memo):
	if i in memo:
		return memo[i]
	num=i

	for x in [2,3,5]:
		while i%x==0:
			i=i//x

	memo[num]=True if i==1 else False
	return memo[num]

n=int(input("enter the ugly number: "))
i=1
count=1
memo={}

while(i>0 and n!=1):
	i+=1
	if is_ugly(i,memo):
		count+=1
	if count==n:
		break
print(i)


