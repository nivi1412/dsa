#dp_besttimetobuyandsell.py
import ast
prices=input("enter the price list:")
prices=ast.literal_eval(prices)

my_min=prices[0]
max_profit=0
mydiff={}
mydiff[0]=max_profit

for i in prices:
	if i < my_min:
		my_min=i
	max_profit=i-my_min
	if max_profit>mydiff[0]:
		mydiff[0]=max_profit
print(mydiff[0])

