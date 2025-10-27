#combination_sum.py
import ast
#[1,2,3] target 7

nums=input("enter the array: ")
nums=ast.literal_eval(nums)
target=int(input("enter the number: "))
my_list=[[]]

#dp[x]= lenght of the list making sum x
dp=[0 for _ in range(target+1)]

dp[0]=1

for total in range(1,target+1,+1):
	for num in nums:
		if num<=target:
			dp[total]+=dp[total-nummko]

	

print(dp)
print(dp[target])