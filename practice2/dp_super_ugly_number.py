
# dp_super_ugly_number.py
import ast

def super_ugly_number(i,primes,memo):
	if i not in memo:
		memo[i]=False
	j=i
	for k in primes:
		while(j%k)==0:
			j=j//k
			if j in memo:
				memo[i]=memo[j]
				j=1
				break
			if j==1: 
				memo[i]=True
				break

	return memo[i]

n=int(input("enter the value of n: "))
primes=input("enter the array of primes: ")
primes=ast.literal_eval(primes)

my_list=[1]
i=1
memo={}
while(len(my_list)!=n):
	i+=1
	if super_ugly_number(i,primes,memo):
		my_list.append(i)


print(memo)
print(my_list[-1])
