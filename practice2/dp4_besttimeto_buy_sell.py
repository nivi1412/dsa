#DP4_besttimeto_buy_sell.py
import ast

my_list=input("enter the price array")
price_list=ast.literal_eval(my_list)

my_dict={}
my_min=price_list[0]
max_profit=0
my_dict[0]=max_profit

for i in range(1,len(price_list),+1):
	if my_min > price_list[i]:
		my_min=price_list[i]
	diff=price_list[i]-my_min
	if diff>my_dict[0]:
		my_dict[0]=diff
print(my_dict[0])


