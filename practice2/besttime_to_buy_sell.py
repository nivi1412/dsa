#besttime_to_buy_sell.py
import ast
import math

prices=input("enter the proces array: ")
prices=ast.literal_eval(prices)

min_price=math.inf
max_profit=-math.inf

for i in range(len(prices)):
	if prices[i]<min_price:
		min_price=prices[i]
	if prices[i]-min_price>max_profit:
		max_profit=prices[i]-min_price


print(max_profit)


