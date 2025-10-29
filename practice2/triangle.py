#triangle.py

import ast
import math
triangle=input("enter the array: ")
triangle=ast.literal_eval(triangle)

for i in range(len(triangle)-2,-1,-1):
	for j in range(len(triangle[i])):
		triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])


print(triangle[0][0])