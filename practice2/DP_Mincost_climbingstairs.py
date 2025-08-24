#DP_Mincost_climbingstairs.py
import ast

def mincost_climbing(cost,n,my_dict)->int: #return my_dict[len(cost)]
	if n in my_dict:
		return my_dict[n]+cost[n]
	my_dict[n]=min(mincost_climbing(cost,n-1,my_dict),mincost_climbing(cost,n-2,my_dict))
	return my_dict[n]+cost[n] if n<len(cost) else my_dict[n]


cost=input("enter the cost array:")
cost=ast.literal_eval(cost)
my_dict={}
my_dict[0]=0
my_dict[1]=0
n=len(cost)
# #bottomsup

# for i in range(2,len(cost)+1,+1):
# 	my_dict[i]=min(cost[i-1]+my_dict[i-1],cost[i-2]+my_dict[i-2])

# print(my_dict[n])

#top down
print(mincost_climbing(cost,n,my_dict))
print(my_dict)