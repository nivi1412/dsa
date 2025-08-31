# DP_Besttime_tobuysellII.py

import ast
price=input("enter the pricelist: ")
prices=ast.literal_eval(price)
profit=0

for i in range(1,len(prices)):
	if prices[i]>prices[i-1]:
		profit+=(prices[i]-prices[i-1])

print(profit)

