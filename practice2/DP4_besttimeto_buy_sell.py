#DP4_besttimeto_buy_sell.py
import ast

my_list=input("enter the price array")
price_list=ast.literal_eval(my_list)

my_dict={}
my_dict["max"]=[0,-1]
my_dict["min"]=[0,10**4]

for i in range(len(price_list)):
	if my_dict["min"][1]>price_list[i]:
		my_dict["min"]=[i,price_list[i]]
	if my_dict["max"][1]<price_list[i] and my_dict["min"][0]<i:
		my_dict["max"]=[i,price_list[i]]

if my_dict["min"][0]==len(price_list)-1:
	print(0)
else:
	print(my_dict["max"][1]-my_dict["min"][1])