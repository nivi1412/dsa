#math9.py
#no of ways to reach from top left corner to bottom right corner
import math

def factorial(num):
	if num==0 or num==1:
		return 1
	if num>1:
		return(num*factorial(num-1))


row=int(input("enter number of rows of grid:"))
col=int(input("enter number of cols of grid:"))

step_no=(row-1)+(col-1)
#no of ways to arrage R and D in step no is step_no C (row-1)

print("possible unique paths are:")
res=factorial(step_no)//(factorial(step_no-(row-1))*factorial(row-1))
print(res)
