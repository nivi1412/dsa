n = 5

# print(1)

# for i in range(2, n + 1):
# 	if i % 2 == 0:
# 		merged_str = str(i + 1)
# 		for j in range(i - 1):
# 			merged_str = merged_str + " " + str(i + 1)
# 	else:
# 		merged_str = str(i - 1)
# 		for j in range(i - 1):
# 			merged_str = merged_str + " " + str(i - 1)
# 	print(merged_str

for i in range(1,n+1):
	for j in range(i):
		if i==1:
			print(i)
		print(i+1) if i%2==0 else print(i-1)