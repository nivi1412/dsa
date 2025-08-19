#DP11_MinCostClimbingStairs.py
import ast

cost=input("enter the array of cost: ")
cost=ast.literal_eval(cost)

first_index=0
second_index=1
count=0

# while(first_index < len(cost) and second_index < len(cost)):
# 	if cost[first_index]<cost[second_index]:
# 		count+=cost[first_index]
# 	else:
# 		count+=cost[second_index]
# 	first_index=second_index
# 	second_index+=1
# if second_index >len(cost):
# 	print(count)

for i in range(len(cost)-2):
	if cost[i]+cost[i+2]>cost[i+1]:
		count+=cost[i+1]
	else:
		count+=cost[i]+cost[i+2]